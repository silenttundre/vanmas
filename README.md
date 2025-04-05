# Vanmas Crew

Welcome to the Vanmas Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Purpose
As a health-conscious parent, ensuring that my children are eating the right foods is a top priority. The CrewAI project was created to help evaluate the nutritional value of food products and determine whether they are beneficial or harmful to our health. By analyzing ingredients and key product features, CrewAI empowers parents like me to make informed decisions about the foods we feed our children. The system considers factors like product category, target brands, and key features—such as low sugar, no artificial colors or flavors, and no preservatives. For example, when looking at breakfast cereals like Honey Bunches of Oats or Kellogg's, CrewAI helps assess if these products meet the health standards I set for my family. This way, I can confidently choose the best food options for my kids' growth and development.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

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

- Modify `src/vanmas/config/agents.yaml` to define your agents
- Modify `src/vanmas/config/tasks.yaml` to define your tasks
- Modify `src/vanmas/crew.py` to add your own logic, tools and specific args
- Modify `src/vanmas/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the vanmas Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The vanmas Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Vanmas Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
