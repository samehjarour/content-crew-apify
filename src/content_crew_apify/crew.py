import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task




@CrewBase
class ContentCrewApifyCrew:
    """ContentCrewApify crew"""

    
    @agent
    def editor_at_apify(self) -> Agent:
        return Agent(
            config=self.agents_config["editor_at_apify"],
            tools=[],
        )
    
    @agent
    def explanation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["explanation_agent"],
            tools=[],
        )
    

    
    @task
    def check_content_against_apify_style_guide(self) -> Task:
        return Task(
            config=self.tasks_config["check_content_against_apify_style_guide"],
        )
    
    @task
    def explain_changes_according_to_apify_style_guide(self) -> Task:
        return Task(
            config=self.tasks_config["explain_changes_according_to_apify_style_guide"],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ContentCrewApify crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
