#!/usr/bin/env python3
"""
Test script for ContentCrewApify crew
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_crew_import():
    """Test if the crew can be imported successfully"""
    try:
        from content_crew_apify.crew import ContentCrewApifyCrew
        print("✅ Crew import successful")
        return True
    except ImportError as e:
        print(f"❌ Crew import failed: {e}")
        return False

def test_crew_initialization():
    """Test if the crew can be initialized"""
    try:
        from content_crew_apify.crew import ContentCrewApifyCrew
        crew_instance = ContentCrewApifyCrew()
        crew = crew_instance.crew()
        
        print(f"✅ Crew initialization successful")
        print(f"   - Agents: {len(crew.agents)}")
        print(f"   - Tasks: {len(crew.tasks)}")
        print(f"   - Process: {crew.process}")
        
        # Validate agents
        for i, agent in enumerate(crew.agents):
            print(f"   - Agent {i+1}: {agent.role}")
        
        # Validate tasks
        for i, task in enumerate(crew.tasks):
            print(f"   - Task {i+1}: {task.description[:50]}...")
        
        return True
    except Exception as e:
        print(f"❌ Crew initialization failed: {e}")
        return False

def test_configuration_files():
    """Test if configuration files are valid"""
    import yaml
    
    config_files = [
        "src/content_crew_apify/config/agents.yaml",
        "src/content_crew_apify/config/tasks.yaml"
    ]
    
    for config_file in config_files:
        try:
            with open(config_file, 'r') as f:
                yaml.safe_load(f)
            print(f"✅ {config_file} is valid")
        except Exception as e:
            print(f"❌ {config_file} is invalid: {e}")
            return False
    
    return True

def test_environment():
    """Test environment setup"""
    env_file = Path(".env")
    
    if not env_file.exists():
        print("❌ .env file not found")
        return False
    
    # Check if API keys are set (not just placeholders)
    with open(env_file, 'r') as f:
        content = f.read()
        
    if "your_openai_api_key_here" in content or "your_anthropic_api_key_here" in content:
        print("⚠️  API keys still contain placeholder values")
        print("   Please update .env with your actual API keys before deployment")
        return False
    
    print("✅ Environment configuration looks good")
    return True

def main():
    """Run all tests"""
    print("🧪 Testing ContentCrewApify Crew")
    print("=" * 40)
    
    tests = [
        ("Configuration Files", test_configuration_files),
        ("Crew Import", test_crew_import),
        ("Crew Initialization", test_crew_initialization),
        ("Environment Setup", test_environment),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} failed")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your crew is ready for deployment.")
        return True
    else:
        print("❌ Some tests failed. Please fix the issues before deploying.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
