from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from vanmas.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class VanmasCrew():
	"""Vanmas crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
            # Uncomment and add tools if needed
        	tools=[SerperDevTool()],
        )

	@agent
	def analysis_agent(self) -> Agent:
		return Agent(
            config=self.agents_config["analysis_agent"],
            verbose=True,
            tools=[],
        )

	@agent
	def recommendation_agent(self) -> Agent:
		return Agent(
            config=self.agents_config["recommendation_agent"],
            verbose=True,
            tools=[],
        )

	@task
	def research_task(self) -> Task:
		return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher(),
        )

	@task
	def analysis_task(self) -> Task:
		return Task(
            config=self.tasks_config["analysis_task"],
            agent=self.analysis_agent(),
        )

	@task
	def recommendation_task(self) -> Task:
		return Task(
            config=self.tasks_config["recommendation_task"],
            agent=self.recommendation_agent(),
        )

	@crew
	def crew(self) -> Crew:
		"""Creates the Vanmas crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)