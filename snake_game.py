from tkinter import *
import random

object_size = 25
row_numbers = 25
column_numbers = 25
game_width = column_numbers * object_size
game_height = row_numbers * object_size
snake_color = "lawn green"
food_color = "red"
snake_body_list = []
FONT = ("Arial", 12, "normal")

class gameObject():

    def __init__(self,coordinate_X,coordinate_Y):
        self.coordinate_X = coordinate_X
        self.coordinate_Y = coordinate_Y


window = Tk()
window.title("Snake Game")
window.resizable(width=False,height=False)

canvas = Canvas(window, width=game_width, height=game_height, bg="black", borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

#open the window on the center
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_X = int((screen_width/2) - (window_width/2))
window_Y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_X}+{window_Y}")

snake = gameObject(5 * object_size, 5 * object_size)
food = gameObject(10 * object_size, 10 * object_size)
snake_vector_X = 0
snake_vector_Y = 0
gameOver_flag = False
score = 0

def snake_moving():
    global snake, food, gameOver_flag , score, snake_body_list

    if (snake.coordinate_X < 0 or snake.coordinate_X >= game_width or snake.coordinate_Y < 0 or snake.coordinate_Y >= game_height):
        gameOver_flag = True
    else:
        gameOver_flag = False

    for snakes in snake_body_list:
        if (snakes.coordinate_X == snake.coordinate_X and snakes.coordinate_Y == snake.coordinate_Y):
            gameOver_flag = True

    if (snake.coordinate_X == food.coordinate_X and snake.coordinate_Y == food.coordinate_Y):
        snake_body_list.append(gameObject(food.coordinate_X, food.coordinate_Y))
        food.coordinate_X = random.randint(2,22) * object_size
        food.coordinate_Y = random.randint(2, 22) * object_size
        score += 1

    for i in range(len(snake_body_list)-1, -1, -1):
        snake_obj = snake_body_list[i]
        if i == 0:
            snake_obj.coordinate_X = snake.coordinate_X
            snake_obj.coordinate_Y = snake.coordinate_Y
        else:
            prev_snake = snake_body_list[i-1]
            snake_obj.coordinate_X = prev_snake.coordinate_X
            snake_obj.coordinate_Y = prev_snake.coordinate_Y

    snake.coordinate_X += snake_vector_X * object_size
    snake.coordinate_Y += snake_vector_Y * object_size

def snake_direction(e): #e = event
    global snake, snake_vector_X,snake_vector_Y

    if (e.keysym == "Up" and snake_vector_Y != 1):
        snake_vector_X = 0
        snake_vector_Y = -1
    elif (e.keysym == "Down" and snake_vector_Y != -1):
        snake_vector_X = 0
        snake_vector_Y = 1
    elif (e.keysym == "Left" and snake_vector_X != 1):
        snake_vector_X = -1
        snake_vector_Y = 0
    elif (e.keysym == "Right" and snake_vector_X != -1):
        snake_vector_X = 1
        snake_vector_Y = 0

def draw_object():
    global snake, food, score, snake_body_list, gameOver_flag
    canvas.delete("all")
    snake_moving()

    # Draw the meal
    canvas.create_rectangle(food.coordinate_X, food.coordinate_Y, food.coordinate_X + object_size,
                            food.coordinate_Y + object_size, fill=food_color)
    # Draw the snake
    canvas.create_rectangle(snake.coordinate_X, snake.coordinate_Y, snake.coordinate_X + object_size,
                            snake.coordinate_Y + object_size, fill=snake_color)

    for snake_ref in snake_body_list:
        canvas.create_rectangle(snake_ref.coordinate_X, snake_ref.coordinate_Y, snake_ref.coordinate_X + object_size, snake_ref.coordinate_Y + object_size, fill="lime green")

    if gameOver_flag == True:
        canvas.create_text(game_width/2,game_height/2,text=f"Game Over\nYour score: {score}",font="Arial 20", fill="white")
    else:
        canvas.create_text(35,20,text=f"Score: {score}", font=FONT, fill="white")
        window.after(125, draw_object)

draw_object()

window.bind("<KeyRelease>", snake_direction)
window.mainloop()