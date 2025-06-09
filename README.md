# ContentCrewApify Crew (Version 2)

Welcome to the ContentCrewApify Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/content_crew_apify/config/agents.yaml` to define your agents
- Modify `src/content_crew_apify/config/tasks.yaml` to define your tasks
- Modify `src/content_crew_apify/crew.py` to add your own logic, tools and specific args
- Modify `src/content_crew_apify/main.py` to add custom inputs for your agents and tasks

## Running the Project

### Local Development

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the content_crew_apify Crew, assembling the agents and assigning them tasks as defined in your configuration.

### Deployment to CrewAI Cloud

To deploy this crew to CrewAI Cloud for production use:

1. **Quick Setup**: Run the setup script to install dependencies and configure your environment:
   ```bash
   ./setup.sh
   ```

2. **Configure API Keys**: Edit the `.env` file and add your API keys:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

3. **Login to CrewAI**:
   ```bash
   crewai login
   ```

4. **Deploy**: Use the automated deployment script:
   ```bash
   python3 deploy.py
   ```

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### What This Crew Does

This crew consists of two specialized agents that work together to enforce Apify's style guide:

1. **Editor Agent**: Reviews content and rewrites it according to Apify's style guide
2. **Explanation Agent**: Identifies changes made and explains which style guide rules were applied

The crew processes content through two sequential tasks:
1. **Content Review**: Checks and edits content against the Apify style guide
2. **Change Explanation**: Provides detailed explanations of the changes made

## Understanding Your Crew

The content_crew_apify Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ContentCrewApify Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

---
*Last updated: June 9, 2025 - Deployment refresh*
