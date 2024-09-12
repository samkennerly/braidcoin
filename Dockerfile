FROM tiagopeixoto/graph-tool:release-2.75
LABEL description="Run Python in Jupyter notebooks with graph-tool."
LABEL maintainer="samkennerly@gmail.com"

# Create a user to launch the Jupyter server
RUN useradd --uid 1001 --create-home braidcoin
WORKDIR /home/braidcoin

# Install system packages
RUN pacman -Syy && pacman -Syy --noconfirm git python-pip

# Install Python packages using --break-system-packages.
# (graph-tool already broke them by installing to system Python)
COPY requirements.txt .
RUN pip install --break-system-packages --upgrade pip && \
    pip install --break-system-packages --requirement requirements.txt

# Ensure Python can find modules in this repo
ENV PYTHONPATH=/home/braidcoin/code

CMD ["/bin/sh"]
