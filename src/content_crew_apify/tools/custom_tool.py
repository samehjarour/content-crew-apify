from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import tempfile
import uuid
from datetime import datetime


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


class ArtifactGeneratorInput(BaseModel):
    """Input schema for ArtifactGenerator."""
    content: str = Field(..., description="The content to save as an artifact")
    filename: str = Field(default="", description="Optional filename for the artifact")

class ArtifactGenerator(BaseTool):
    name: str = "artifact_generator"
    description: str = (
        "Creates downloadable artifacts from content and provides shareable links. "
        "Useful for saving edited content, reports, or any text-based output as files."
    )
    args_schema: Type[BaseModel] = ArtifactGeneratorInput

    def _run(self, content: str, filename: str = "") -> str:
        try:
            # Generate unique filename if not provided
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                unique_id = str(uuid.uuid4())[:8]
                filename = f"apify_content_{timestamp}_{unique_id}.md"
            elif not filename.endswith('.md'):
                filename += '.md'
            
            # Create artifacts directory if it doesn't exist
            artifacts_dir = os.path.join(os.getcwd(), "artifacts")
            os.makedirs(artifacts_dir, exist_ok=True)
            
            # Write content to file
            file_path = os.path.join(artifacts_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Create a shareable link format
            artifact_link = f"file://{file_path}"
            
            return f"Artifact created successfully!\n\n**Download Link:** {artifact_link}\n**Filename:** {filename}\n**Location:** {file_path}"
            
        except Exception as e:
            return f"Error creating artifact: {str(e)}"
