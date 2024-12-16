
# Pong Game with Flask

This project is a simple Pong game implemented using HTML, JavaScript, and Flask. It is designed to demonstrate basic web development concepts such as canvas manipulation, event handling, and server-side routing.

----------

## Project Structure

```bash
Pong-Game/
|-- static/
|   |-- 
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
git clone https://github.com/sugeng-riyanto/pong-game-using-flask-python.git
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
        const canvas = document.getElementById('pongCanvas'); // Get the canvas element
        const ctx = canvas.getContext('2d'); // Get the 2D drawing context for the canvas
        canvas.width = 800; // Set canvas width
        canvas.height = 600; // Set canvas height

        // Game state variables
        let isRunning = true; // Indicates if the game is running
        let playerScore = 0; // Tracks player's score
        let aiScore = 0; // Tracks AI's score
        let timeLeft = 60; // Timer for the game

        // Ball properties
        const ball = {
            x: canvas.width / 2, // Ball's initial X position (center)
            y: canvas.height / 2, // Ball's initial Y position (center)
            radius: 10, // Ball's radius
            dx: 4, // Ball's horizontal speed
            dy: 4 // Ball's vertical speed
        };

        // Paddle properties
        const paddleWidth = 10; // Paddle width
        const paddleHeight = 100; // Paddle height
        const player = { x: 0, y: canvas.height / 2 - paddleHeight / 2, dy: 0 }; // Player's paddle properties
        const ai = { x: canvas.width - paddleWidth, y: canvas.height / 2 - paddleHeight / 2 }; // AI's paddle properties

        // Timer function
        function startTimer() {
            const timer = setInterval(() => {
                if (!isRunning || timeLeft <= 0) { // Stop timer if game is not running or time is up
                    clearInterval(timer); // Clear the timer
                    isRunning = false; // Stop the game
                    alert('Game Over! Final Score: Player ' + playerScore + ' - AI ' + aiScore); // Display final score
                } else {
                    timeLeft--; // Decrease time
                    document.getElementById('timer').textContent = timeLeft; // Update timer display
                }
            }, 1000); // Timer interval (1 second)
        }

        // Draw the ball on the canvas
        function drawBall() {
            ctx.beginPath(); // Start drawing path
            ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2); // Draw a circle for the ball
            ctx.fillStyle = '#fff'; // Set ball color to white
            ctx.fill(); // Fill the ball
            ctx.closePath(); // End drawing path
        }

        // Draw a paddle on the canvas
        function drawPaddle(x, y) {
            ctx.fillStyle = '#fff'; // Set paddle color to white
            ctx.fillRect(x, y, paddleWidth, paddleHeight); // Draw paddle rectangle
        }

        // Move the ball
        function moveBall() {
            ball.x += ball.dx; // Update ball's X position
            ball.y += ball.dy; // Update ball's Y position

            // Bounce on top/bottom edges
            if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
                ball.dy *= -1; // Reverse vertical direction
            }

            // Bounce on paddles
            if (
                (ball.x - ball.radius < player.x + paddleWidth && ball.y > player.y && ball.y < player.y + paddleHeight) ||
                (ball.x + ball.radius > ai.x && ball.y > ai.y && ball.y < ai.y + paddleHeight)
            ) {
                ball.dx *= -1; // Reverse horizontal direction
            }

            // Score logic
            if (ball.x - ball.radius < 0) { // Ball goes past player paddle
                aiScore++; // Increment AI score
                resetBall(); // Reset ball position
            } else if (ball.x + ball.radius > canvas.width) { // Ball goes past AI paddle
                playerScore++; // Increment player score
                resetBall(); // Reset ball position
            }

            // Update score display
            document.getElementById('playerScore').textContent = playerScore;
            document.getElementById('aiScore').textContent = aiScore;
        }

        // Reset ball to the center
        function resetBall() {
            ball.x = canvas.width / 2; // Reset X position
            ball.y = canvas.height / 2; // Reset Y position
            ball.dx *= -1; // Reverse horizontal direction
        }

        // Move player's paddle
        function movePlayer() {
            player.y += player.dy; // Update player's Y position
            if (player.y < 0) player.y = 0; // Prevent paddle from going above canvas
            if (player.y + paddleHeight > canvas.height) player.y = canvas.height - paddleHeight; // Prevent paddle from going below canvas
        }

        // Move AI's paddle
        function moveAI() {
            if (ball.y < ai.y + paddleHeight / 2) ai.y -= 3; // Move AI paddle up
            if (ball.y > ai.y + paddleHeight / 2) ai.y += 3; // Move AI paddle down
            if (ai.y < 0) ai.y = 0; // Prevent AI paddle from going above canvas
            if (ai.y + paddleHeight > canvas.height) ai.y = canvas.height - paddleHeight; // Prevent AI paddle from going below canvas
        }

        // Game loop to update and render the game
        function gameLoop() {
            if (isRunning) { // Continue only if the game is running
                ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas

                drawBall(); // Draw the ball
                drawPaddle(player.x, player.y); // Draw player's paddle
                drawPaddle(ai.x, ai.y); // Draw AI's paddle

                moveBall(); // Update ball position
                movePlayer(); // Update player's paddle position
                moveAI(); // Update AI's paddle position

                requestAnimationFrame(gameLoop); // Call gameLoop recursively for the next frame
            }
        }

        // Control player's paddle with keyboard
        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowUp') player.dy = -5; // Move paddle up
            if (e.key === 'ArrowDown') player.dy = 5; // Move paddle down
        });

        window.addEventListener('keyup', () => {
            player.dy = 0; // Stop paddle movement
        });

        // Buttons to control the game
        document.getElementById('continueBtn').addEventListener('click', () => {
            if (!isRunning) { // Continue only if the game is not running
                isRunning = true; // Resume the game
                gameLoop(); // Start the game loop
            }
        });

        document.getElementById('stopBtn').addEventListener('click', () => {
            isRunning = false; // Stop the game
        });

        // Start the game and timer
        gameLoop(); // Begin the game loop
        startTimer(); // Begin the timer
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
