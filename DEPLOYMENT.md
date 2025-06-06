# ContentCrewApify Deployment Guide

This guide will help you deploy your ContentCrewApify crew to CrewAI Cloud.

## Prerequisites

1. **CrewAI Account**: Sign up at [CrewAI Cloud](https://cloud.crewai.com)
2. **API Keys**: You'll need API keys for the LLMs used by your agents
3. **CrewAI CLI**: Install the CrewAI command-line interface

## Installation

### 1. Install CrewAI CLI

```bash
pip install crewai
```

### 2. Login to CrewAI

```bash
crewai login
```

### 3. Set up Environment Variables

Edit the `.env` file and add your API keys:

```bash
# Required API keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional: Disable telemetry
CREWAI_TELEMETRY_OPT_OUT=true
```

## Deployment Options

### Option 1: Automated Deployment (Recommended)

Use the provided deployment script:

```bash
python3 deploy.py
```

This script will:
- Check all requirements
- Validate your crew configuration
- Deploy to CrewAI Cloud
- Provide next steps

### Option 2: Manual Deployment

#### Step 1: Validate Your Crew Locally

```bash
crewai run
```

#### Step 2: Deploy to CrewAI Cloud

```bash
crewai deploy
```

#### Step 3: Configure Environment Variables

In the CrewAI dashboard:
1. Navigate to your deployed crew
2. Go to Settings > Environment Variables
3. Add your API keys:
   - `OPENAI_API_KEY`
   - `ANTHROPIC_API_KEY`

### Option 3: Docker Deployment

If you prefer containerized deployment:

#### Build the Docker image:

```bash
docker build -t content-crew-apify .
```

#### Run locally for testing:

```bash
docker run -e OPENAI_API_KEY=your_key -e ANTHROPIC_API_KEY=your_key content-crew-apify
```

#### Deploy to your preferred container platform (AWS ECS, Google Cloud Run, etc.)

## Configuration

### Crew Configuration

Your crew is configured in:
- `src/content_crew_apify/config/agents.yaml` - Agent definitions
- `src/content_crew_apify/config/tasks.yaml` - Task definitions
- `src/content_crew_apify/crew.py` - Crew logic

### Deployment Configuration

The deployment is configured in:
- `crewai.yaml` - CrewAI Cloud deployment settings
- `pyproject.toml` - Python project configuration
- `Dockerfile` - Container configuration (if using Docker)

## Usage

### Running Your Deployed Crew

Once deployed, you can run your crew through:

1. **CrewAI Dashboard**: Use the web interface to trigger runs
2. **API Calls**: Use the CrewAI API to programmatically run your crew
3. **Webhooks**: Set up webhooks for automated triggers

### Example API Usage

```python
import requests

# Replace with your actual crew endpoint
crew_endpoint = "https://api.crewai.com/v1/crews/your-crew-id/run"

# Your input data
inputs = {
    "content": "Your content to be edited according to Apify style guide"
}

response = requests.post(
    crew_endpoint,
    json={"inputs": inputs},
    headers={"Authorization": "Bearer your-api-token"}
)

result = response.json()
print(result)
```

## Monitoring and Troubleshooting

### Logs

Access logs through:
- CrewAI Dashboard > Your Crew > Logs
- CLI: `crewai logs <crew-id>`

### Common Issues

1. **Authentication Errors**
   - Ensure API keys are correctly set in environment variables
   - Check that keys have sufficient permissions

2. **Import Errors**
   - Verify all dependencies are listed in `pyproject.toml`
   - Check Python version compatibility (3.10-3.12)

3. **Configuration Errors**
   - Validate YAML syntax in config files
   - Ensure agent and task names match between files

### Health Checks

The deployment includes health checks to monitor your crew:
- HTTP endpoint: `/health`
- Interval: 30 seconds
- Timeout: 10 seconds

## Scaling and Performance

### Memory and CPU

Adjust resources in `crewai.yaml`:

```yaml
runtime:
  memory: "2GB"  # Increase for larger workloads
  cpu: "1000m"   # Increase for better performance
```

### Timeout Settings

Adjust timeout for longer-running tasks:

```yaml
runtime:
  timeout: "600s"  # 10 minutes
```

## Security

### Environment Variables

- Never commit API keys to version control
- Use CrewAI's secure environment variable storage
- Rotate keys regularly

### Network Security

- CrewAI Cloud provides secure HTTPS endpoints
- API tokens are required for access
- Rate limiting is automatically applied

## Support

For deployment issues:

1. Check the [CrewAI Documentation](https://docs.crewai.com)
2. Visit the [CrewAI GitHub Repository](https://github.com/joaomdmoura/crewai)
3. Join the [CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)

## Next Steps

After successful deployment:

1. **Test Your Crew**: Run a few test cases to ensure everything works
2. **Set Up Monitoring**: Configure alerts for failures or performance issues
3. **Integrate**: Connect your crew to your existing workflows
4. **Optimize**: Monitor performance and adjust resources as needed

---

Your ContentCrewApify crew is now ready for deployment! 🚀
