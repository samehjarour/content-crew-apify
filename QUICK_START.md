# Quick Start Guide - ContentCrewApify Deployment

## TL;DR - Fast Deployment

```bash
# 1. Install dependencies (if needed)
pip3 install crewai --user

# 2. Update API keys in .env file
# Edit .env and replace placeholder values with your actual API keys

# 3. Login to CrewAI
crewai login

# 4. Deploy (choose one option)
python3 simple_deploy.py    # Recommended - simpler
# OR
python3 deploy.py          # Full validation version
```

## Step-by-Step Instructions

### 1. Install CrewAI CLI
```bash
pip3 install crewai --user
```

### 2. Configure API Keys
Edit the `.env` file and replace the placeholder values:
```bash
OPENAI_API_KEY=sk-your-actual-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-actual-anthropic-key-here
```

### 3. Login to CrewAI
```bash
crewai login
```
Follow the prompts to authenticate with your CrewAI account.

### 4. Deploy Your Crew
Choose one of these deployment options:

#### Option A: Simple Deployment (Recommended)
```bash
python3 simple_deploy.py
```

#### Option B: Full Deployment with Validation
```bash
python3 deploy.py
```

#### Option C: Manual Deployment
```bash
crewai deploy
```

## Troubleshooting

### Command Not Found: python
- Use `python3` instead of `python` on macOS/Linux
- On Windows, use `python` or `py`

### Permission Denied
- Add `--user` flag: `pip3 install crewai --user`
- Or use a virtual environment

### Import Errors
- Make sure CrewAI is installed: `pip3 install crewai --user`
- Check Python version: `python3 --version` (should be 3.10-3.12)

### Deployment Fails
1. Ensure you're logged in: `crewai login`
2. Check your internet connection
3. Verify API keys are set correctly in `.env`
4. Make sure you have a CrewAI account

## What Happens After Deployment

1. Your crew will be deployed to CrewAI Cloud
2. You can access it via the CrewAI dashboard
3. Set up any additional environment variables in the dashboard
4. Test your crew with sample content
5. Monitor logs and performance

## Your Crew's Purpose

This ContentCrewApify crew:
- **Editor Agent**: Reviews and rewrites content according to Apify's style guide
- **Explanation Agent**: Explains changes made and references style guide rules

Perfect for ensuring all Apify content follows the company's writing standards!

---

Need help? Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.
