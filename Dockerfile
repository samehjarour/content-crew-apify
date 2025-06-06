FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install UV package manager
RUN pip install uv

# Copy project files
COPY pyproject.toml ./
COPY src/ ./src/
COPY knowledge/ ./knowledge/

# Install dependencies
RUN uv pip install --system -e .

# Create non-root user
RUN useradd --create-home --shell /bin/bash crewai
USER crewai

# Expose port (if needed for API endpoints)
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app/src
ENV CREWAI_TELEMETRY_OPT_OUT=true

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Default command
CMD ["python", "-m", "content_crew_apify.main", "run"]
