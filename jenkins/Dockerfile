FROM jenkins/inbound-agent:latest

# Set the user to root to allow package installation
USER root

# Update package list and install Python 3.10 and required dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Verify Python installation
RUN python3.10 --version && pip3 --version

# Switch back to Jenkins user for security
USER jenkins

#ENV JENKINS_URL=$URL
#ENV JENKINS_SECRET=$SECRET
#ENV JENKINS_AGENT_NAME=linux-agent

# Entry point (starts the Jenkins agent)
CMD ["jenkins-agent"]