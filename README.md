# Alphabet Animation Setup and Running Guide

This guide provides instructions for setting up and running the Alphabet Animation script using Pygame.

## Requirements

- Python 3.x
- Pygame

## Setup

1. Clone or download the repository containing the Python script.

2. Navigate to the project directory:

    ```bash
    cd loader
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    - On Windows:
    
        ```bash
        .venv\Scripts\activate
        ```
    
    - On macOS and Linux:
    
        ```bash
        source .venv/bin/activate
        ```

5. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Script

1. Ensure that you are in the project directory and the virtual environment is activated.

2. Run the Python script:

    ```bash
    python loader.py
    ```

3. The animation will start, displaying letters of the alphabet in a loop. Press the close button (X) on the window to exit the animation.

## Deactivating the Virtual Environment

When you're finished running the script, you can deactivate the virtual environment:

```bash
deactivate
