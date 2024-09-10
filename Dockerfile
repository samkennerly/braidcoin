FROM tiagopeixoto/graph-tool:release-2.75
LABEL description="Run Python in Jupyter notebooks with graph-tool."
LABEL maintainer="samkennerly@gmail.com"

# Install system packages
RUN pacman -Syy && pacman -Syy --noconfirm git python-pip

# Install Python packages using --break-system-packages.
# (graph-tool already broke them by installing to system Python)
COPY requirements.txt .
RUN pip install --break-system-packages --upgrade pip && \
    pip install --break-system-packages --requirement requirements.txt

# Create user and run as that user
RUN useradd --uid 1001 braidcoin
USER braidcoin
WORKDIR /home/braidcoin

RUN mkdir .ipython .jupyter books code output

# Ensure Python can find modules in this repo
ENV PYTHONPATH=/home/braidcoin/code

CMD ["/bin/sh"]
