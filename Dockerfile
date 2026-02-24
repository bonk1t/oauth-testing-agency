FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/root/.local/bin:${PATH}"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/activity-logs \
    /app/data/oauth-tokens \
    /app/github_agent/files \
    /app/github_agent/tools && \
    chmod -R a+rwx /app/activity-logs /app/data/oauth-tokens /app/github_agent/files /app/github_agent/tools

CMD ["python", "-u", "main.py"]