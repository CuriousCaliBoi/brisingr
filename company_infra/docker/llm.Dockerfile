FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Base Python dependencies
COPY env/base-requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/base-requirements.txt

# LLM-specific dependencies
COPY env/llm-requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/llm-requirements.txt

# Copy project
WORKDIR /app
COPY . .

CMD ["bash"]
