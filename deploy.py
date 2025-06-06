#!/usr/bin/env python3
"""
Deployment script for ContentCrewApify to CrewAI Cloud
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_requirements():
    """Check if all required tools and configurations are present"""
    print("🔍 Checking deployment requirements...")
    
    # Check if crewai CLI is installed
    try:
        result = subprocess.run(['crewai', '--version'], capture_output=True, text=True)
        print(f"✅ CrewAI CLI found: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ CrewAI CLI not found. Install with: pip install crewai")
        return False
    
    # Check if .env file exists
    if not Path('.env').exists():
        print("❌ .env file not found. Please create it with your API keys.")
        return False
    else:
        print("✅ .env file found")
    
    # Check if required files exist
    required_files = ['pyproject.toml', 'src/content_crew_apify/crew.py', 'crewai.yaml']
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ Required file not found: {file}")
            return False
        else:
            print(f"✅ {file} found")
    
    return True

def validate_configuration():
    """Validate the crew configuration"""
    print("\n🔧 Validating crew configuration...")
    
    try:
        # Try to import and validate the crew
        sys.path.insert(0, 'src')
        from content_crew_apify.crew import ContentCrewApifyCrew
        
        crew_instance = ContentCrewApifyCrew()
        crew = crew_instance.crew()
        
        print(f"✅ Crew validation successful")
        print(f"   - Agents: {len(crew.agents)}")
        print(f"   - Tasks: {len(crew.tasks)}")
        
        return True
    except Exception as e:
        print(f"❌ Crew validation failed: {e}")
        return False

def deploy_to_crewai():
    """Deploy the crew to CrewAI Cloud"""
    print("\n🚀 Deploying to CrewAI Cloud...")
    
    try:
        # Login check
        print("Checking CrewAI authentication...")
        result = subprocess.run(['crewai', 'login', '--help'], capture_output=True, text=True)
        if "Sign Up/Login to CrewAI+" not in result.stdout:
            print("Please login to CrewAI first:")
            print("crewai login")
            return False
        
        # Deploy the crew
        print("Deploying crew...")
        result = subprocess.run(['crewai', 'deploy'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Deployment successful!")
            print(result.stdout)
            return True
        else:
            print("❌ Deployment failed:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Deployment error: {e}")
        return False

def main():
    """Main deployment function"""
    print("🎯 ContentCrewApify Deployment Script")
    print("=" * 40)
    
    # Step 1: Check requirements
    if not check_requirements():
        print("\n❌ Requirements check failed. Please fix the issues above.")
        sys.exit(1)
    
    # Step 2: Validate configuration
    if not validate_configuration():
        print("\n❌ Configuration validation failed. Please fix the issues above.")
        sys.exit(1)
    
    # Step 3: Deploy
    if not deploy_to_crewai():
        print("\n❌ Deployment failed. Please check the errors above.")
        sys.exit(1)
    
    print("\n🎉 Deployment completed successfully!")
    print("\nNext steps:")
    print("1. Set your API keys in the CrewAI dashboard")
    print("2. Test your crew deployment")
    print("3. Monitor logs and performance")

if __name__ == "__main__":
    main()
