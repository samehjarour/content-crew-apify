#!/bin/bash

# ContentCrewApify Setup Script
echo "🎯 Setting up ContentCrewApify for deployment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if UV is installed, install if not
if ! command -v uv &> /dev/null; then
    echo "📦 Installing UV package manager..."
    pip3 install uv --user
else
    echo "✅ UV package manager found"
fi

# Install dependencies using UV
echo "📦 Installing project dependencies..."
if command -v uv &> /dev/null; then
    uv pip install -e .
else
    echo "📦 Installing dependencies with pip3..."
    pip3 install -e . --user
fi

# Install CrewAI CLI if not present
if ! command -v crewai &> /dev/null; then
    echo "📦 Installing CrewAI CLI..."
    pip3 install crewai --user
else
    echo "✅ CrewAI CLI found"
fi

# Check if .env file has been configured
if grep -q "your_.*_api_key_here" .env; then
    echo "⚠️  Please update your API keys in the .env file before deploying"
    echo "   Edit .env and replace the placeholder values with your actual API keys"
else
    echo "✅ API keys appear to be configured"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Update your API keys in .env file (if not done already)"
echo "2. Login to CrewAI: crewai login"
echo "3. Deploy your crew: python3 deploy.py"
echo ""
echo "For detailed instructions, see DEPLOYMENT.md"
