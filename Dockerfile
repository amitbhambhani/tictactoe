# Use base python image
FROM python:3.13

# Copy repo into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run program
CMD ["python3", "./tictactoe.py"]

