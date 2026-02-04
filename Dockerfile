FROM apify/actor-python:3.11

# Copy requirements first for better caching
COPY requirements.txt ./

# Install Python dependencies
RUN echo "Python version:" \
    && python --version \
    && echo "Pip version:" \
    && pip --version \
    && echo "Installing dependencies from requirements.txt:" \
    && pip install --no-cache-dir -r requirements.txt \
    && echo "All installed Python packages:" \
    && pip freeze

# Install Playwright browsers
RUN playwright install

# Copy the rest of the source code
COPY . ./

# Set the entry point
CMD python3 main.py
