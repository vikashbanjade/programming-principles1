import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Simple Paddle Game")

# Set the window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# Paddle properties
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
PADDLE_COLOR = "white"
paddle_x = WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = WINDOW_HEIGHT - 30

# Ball properties
BALL_SIZE = 20
BALL_COLOR = "white"
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = random.choice([-5, 5])
ball_dy = -5

# Draw the paddle
paddle = canvas.create_rectangle(paddle_x, paddle_y, paddle_x + PADDLE_WIDTH, paddle_y + PADDLE_HEIGHT, fill=PADDLE_COLOR)

# Draw the ball
ball = canvas.create_oval(ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2,
                          ball_x + BALL_SIZE // 2, ball_y + BALL_SIZE // 2,
                          fill=BALL_COLOR)

# Game loop
def game_loop():
    global paddle_x, ball_x, ball_y, ball_dx, ball_dy

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with walls
    if ball_x - BALL_SIZE // 2 < 0 or ball_x + BALL_SIZE // 2 > WINDOW_WIDTH:
        ball_dx = -ball_dx
    if ball_y - BALL_SIZE // 2 < 0:
        ball_dy = -ball_dy

    # Check for collision with paddle
    if ball_y + BALL_SIZE // 2 >= paddle_y and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
        ball_dy = -ball_dy

    # Update the ball position
    canvas.coords(ball, ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2,
                  ball_x + BALL_SIZE // 2, ball_y + BALL_SIZE // 2)

    # Schedule the next frame
    root.after(10, game_loop)

# Move the paddle
def move_paddle(event):
    global paddle_x
    paddle_x = event.x - PADDLE_WIDTH // 2
    canvas.coords(paddle, paddle_x, paddle_y, paddle_x + PADDLE_WIDTH, paddle_y + PADDLE_HEIGHT)

# Bind the paddle movement to the mouse motion
canvas.bind("<Motion>", move_paddle)

# Start the game loop
game_loop()

# Start the event loop
root.mainloop()