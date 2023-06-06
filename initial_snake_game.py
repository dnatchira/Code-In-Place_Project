from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
SIZE_tail = 15
VELOCITY = 20

def main():
    DELAY = 0.15
    point = 0
    obstacles = []
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    text1 = canvas.create_text(CANVAS_WIDTH/2-70, CANVAS_HEIGHT/2-20, text='Welcome to', font_size = 25, font = 'Ubuntu')
    text2 = canvas.create_text(CANVAS_WIDTH/2-105, CANVAS_HEIGHT/2+20, text='Baby Snake Game!', font_size = 25, font = 'Ubuntu')
    # draw a player
    snake_x = 0
    snake_y = 0
    snake = canvas.create_rectangle(snake_x, snake_y, SIZE, SIZE, 'Blue')
    
    # draw a goal
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    goal = canvas.create_rectangle(20*x, 20*y, 20*x+SIZE, 20*y+SIZE, 'Salmon')
    
    while True:
        key1 = canvas.get_last_key_press()
        if key1 == 'ArrowRight' or key1 == 'ArrowLeft' or key1 == 'ArrowUp' or key1 == 'ArrowDown':
            canvas.delete(text1)
            canvas.delete(text2)
            break

    while True:
        if key1 == "ArrowRight":
            snake_x += VELOCITY
            canvas.moveto(snake, snake_x, snake_y)
            time.sleep(DELAY)
            key2 = canvas.get_last_key_press()
            if key2 == 'ArrowLeft' or key2 == 'ArrowDown' or key2 == 'ArrowUp':
                key1 = key2
                
        
        elif key1 == 'ArrowLeft':
            snake_x -= VELOCITY
            canvas.moveto(snake, snake_x, snake_y)
            time.sleep(DELAY)
            key2 = canvas.get_last_key_press()
            if key2 == 'ArrowRight' or key2 == 'ArrowDown' or key2 == 'ArrowUp':
                key1 = key2
                
        elif key1 == 'ArrowUp':
            snake_y -= VELOCITY
            canvas.moveto(snake, snake_x, snake_y)
            time.sleep(DELAY)
            key2 = canvas.get_last_key_press()
            if key2 == 'ArrowLeft' or key2 == 'ArrowDown' or key2 == 'ArrowRight':
                key1 = key2
                

        elif key1 == 'ArrowDown':
            snake_y += VELOCITY
            canvas.moveto(snake, snake_x, snake_y)
            time.sleep(DELAY)
            key2 = canvas.get_last_key_press()
            if key2 == 'ArrowLeft' or key2 == 'ArrowRight' or key2 == 'ArrowUp':
                key1 = key2
            
        if snake_x < 0 or snake_x > 400 or snake_y < 0 or snake_y > 400:
            text1 = canvas.create_text(CANVAS_WIDTH/2-70, CANVAS_HEIGHT/2-20, text='Game Over!', font_size = 25, font = 'Ubuntu')
            text2 = canvas.create_text(CANVAS_WIDTH/2-80, CANVAS_HEIGHT/2+20, text='Your score is '+str(point), font_size = 25, font = 'Ubuntu')
            break
        
        goal_top_y = canvas.get_top_y(goal)
        goal_left_x = canvas.get_left_x(goal)
        
        if (goal_left_x == snake_x) & (goal_top_y == snake_y):
            canvas.moveto(goal, 20*random.randint(0,19), 20*random.randint(0,19))
            if DELAY > 0.03:
                DELAY -= 0.01 # get faster each time touches the goal
            point += 1 # keep track of points
            # add obstacle each time touches the goal
            x = random.randint(0, 19)
            y = random.randint(0, 19)
            canvas.create_rectangle(20*x, 20*y, 20*x+SIZE, 20*y+SIZE, 'gray')
            obstacles = canvas.find_overlapping(0, 0, 400, 400)
        
        # check touch the obstacle
        for object in obstacles:
            if (object != 'shape_2') & (object != 'shape_3'):
                if (snake_x == canvas.get_left_x(object)) & (snake_y == canvas.get_top_y(object)):
                    text1 = canvas.create_text(CANVAS_WIDTH/2-70, CANVAS_HEIGHT/2-20, text='Game Over!', font_size = 25, font = 'Ubuntu')
                    text2 = canvas.create_text(CANVAS_WIDTH/2-80, CANVAS_HEIGHT/2+20, text='Your score is '+str(point), font_size = 25, font = 'Ubuntu')
                    return
    
if __name__ == '__main__':
    main()
