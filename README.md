
# Pong Game with Flask

This project is a simple Pong game implemented using HTML, JavaScript, and Flask. It is designed to demonstrate basic web development concepts such as canvas manipulation, event handling, and server-side routing.

----------

## Project Structure

```git
Pong-Game/
|-- static/
|   |-- index.html
|-- templates/
|   |-- index.html
|-- app.py
|-- README.md
```

1.  **index.html**: The front-end of the Pong game using HTML5 Canvas.
    
2.  **app.py**: A Flask application that serves the HTML page.
    
3.  **README.md**: Documentation for setting up and running the project.
    

----------

## Prerequisites

1.  Python 3.x installed on your system.
    
2.  Flask library installed.
    
3.  A browser to run the Pong game.
    

----------

## Setup and Installation

### Step 1: Clone the Repository

```
git clone https://github.com/your-repo/Pong-Game.git
cd Pong-Game
```

### Step 2: Install Dependencies

Install Flask using pip:

```bash
pip install flask
```

### Step 3: Run the Flask Application

Run the following command to start the Flask server:

```bash
python app.py
```

The application will be hosted locally at:

```bash
http://0.0.0.0:8080
```

----------

## How to Play

1.  Open your browser and navigate to `http://0.0.0.0:8080`.
    
2.  Use the **Arrow Up** and **Arrow Down** keys to move the player's paddle.
    
3.  The AI paddle moves automatically.
    
4.  Score points by bouncing the ball past the AI paddle.
    

### Controls

-   **Arrow Up**: Move paddle up.
    
-   **Arrow Down**: Move paddle down.
    

----------

## Features

1.  **Timer**: Counts down from 60 seconds.
    
2.  **Score Tracking**: Displays the scores for both the player and the AI.
    
3.  **Pause and Resume**: Control the game using the `Continue` and `Stop` buttons.
    

----------

## Code Overview

### `index.html`

This file contains the game's front-end logic, including:

-   **HTML Structure**:
    
    ```html
    <!DOCTYPE html> <!-- Declares the document type -->
    <html lang="en"> <!-- Sets the language to English -->
    <head> <!-- Contains metadata and styles -->
        <meta charset="UTF-8"> <!-- Specifies character encoding -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Makes the page responsive -->
        <title>Pong Game</title> <!-- Title of the game -->
        <style>
            body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; text-align: center; background-color: #000; color: #fff; } <!-- Body styling -->
            canvas { display: block; margin: 20px auto; background: #111; } <!-- Canvas styling -->
            #controls { margin-top: 10px; } <!-- Control buttons styling -->
            button { margin: 5px; padding: 10px 20px; font-size: 16px; cursor: pointer; } <!-- Button styling -->
        </style>
    </head>
    <body>
        <h1>Pong Game</h1> <!-- Game title -->
        <div id="info"> <!-- Displays timer and scores -->
            <p>Time Left: <span id="timer">60</span> seconds</p>
            <p>Player Score: <span id="playerScore">0</span> | AI Score: <span id="aiScore">0</span></p>
        </div>
        <canvas id="pongCanvas"></canvas> <!-- Canvas for the game -->
        <div id="controls"> <!-- Buttons to control the game -->
            <button id="continueBtn">Continue</button>
            <button id="stopBtn">Stop</button>
        </div>
        <script>
            // JavaScript for game logic, including:
            // - Ball movement
            // - Paddle controls
            // - Timer countdown
            // - Collision detection
        </script>
    </body>
    </html>
    ```
    

### `app.py`

This file serves the HTML page using Flask.

-   **Imports**:
    
    ```python
    from flask import Flask, render_template # Flask to create the server, render_template to serve HTML
    ```
    
-   **Flask Application Setup**:
    
    ```python
    app = Flask(__name__) # Initialize Flask app
    ```
    
-   **Route Definition**:
    
    ```python
    @app.route("/") # Define the home route
    def index():
        return render_template("index.html") # Render the game page
    ```
    
-   **Run the Application**:
    
    ```python
    if __name__ == "__main__":
        app.run('0.0.0.0',8080) # Run Flask app on specified port
    ```
    

----------

## Customization

1.  **Ball Speed**: Modify `ball.dx` and `ball.dy` values in the JavaScript section.
    
2.  **Timer**: Adjust the `timeLeft` variable in the JavaScript to set a different game duration.
    
3.  **Paddle Size**: Change the `paddleHeight` variable in the JavaScript section.
    

----------

## Learning Outcomes

By completing this project, you will learn:

1.  Basics of HTML5 Canvas for game development.
    
2.  Handling user input with JavaScript.
    
3.  Setting up a simple Flask server.
    
4.  Combining front-end and back-end technologies.
    

----------

## Troubleshooting

-   **Flask not installed**: Run `pip install flask` to install Flask.
    
-   **Port already in use**: Change the port in `app.py` to a different value (e.g., `8081`).
    
-   **Game not responding**: Ensure the browser supports HTML5 and JavaScript is enabled.
    

----------

## Acknowledgments

-   Flask Documentation: https://flask.palletsprojects.com/
    
-   HTML5 Canvas Guide: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
    

----------

## License

This project is open-source and available under the MIT License.
