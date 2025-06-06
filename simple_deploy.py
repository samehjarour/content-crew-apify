#!/usr/bin/env python3
"""
Simple deployment script for ContentCrewApify to CrewAI Cloud
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Simple deployment function"""
    print("🎯 ContentCrewApify Simple Deployment")
    print("=" * 40)
    
    # Check if .env file exists
    if not Path('.env').exists():
        print("❌ .env file not found. Please create it with your API keys.")
        sys.exit(1)
    
    # Check if API keys are configured
    with open('.env', 'r') as f:
        content = f.read()
        
    if "your_openai_api_key_here" in content or "your_anthropic_api_key_here" in content:
        print("❌ Please update your API keys in the .env file before deploying")
        print("   Edit .env and replace the placeholder values with your actual API keys")
        sys.exit(1)
    
    print("✅ Environment configuration looks good")
    
    # Check if crewai CLI is available
    try:
        result = subprocess.run(['crewai', '--version'], capture_output=True, text=True)
        print(f"✅ CrewAI CLI found: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ CrewAI CLI not found. Please install it first:")
        print("   pip3 install crewai --user")
        sys.exit(1)
    
    print("\n🚀 Deploying to CrewAI Cloud...")
    print("Note: Make sure you've logged in with 'crewai login' first")
    
    # Deploy the crew
    try:
        result = subprocess.run(['crewai', 'deploy'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Deployment successful!")
            print(result.stdout)
        else:
            print("❌ Deployment failed:")
            print(result.stderr)
            print("\nTroubleshooting tips:")
            print("1. Make sure you're logged in: crewai login")
            print("2. Check your internet connection")
            print("3. Verify your project structure is correct")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Deployment error: {e}")
        sys.exit(1)
    
    print("\n🎉 Deployment completed successfully!")
    print("\nNext steps:")
    print("1. Set your API keys in the CrewAI dashboard")
    print("2. Test your crew deployment")
    print("3. Monitor logs and performance")

if __name__ == "__main__":
    main()
