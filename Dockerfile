# Step 1: Use a tiny, secure, lightweight Python image
FROM python:3.10-slim

# Step 2: Create and set the folder inside the container
WORKDIR /app

# Step 3: Copy your script into the container workspace
COPY treasure_island.py /app/

# Step 4: Run the game interactively when the container fires up
# We use the -u flag for unbuffered output so text prints instantly in the console
CMD ["python", "-u", "treasure_island.py"]