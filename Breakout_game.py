import graphics
import time
import random
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH-BRICK_GAP*9) / 10
BRICK_HEIGHT = 10
change_x = 10
change_y = 10
START_X = CANVAS_WIDTH/2
START_Y = CANVAS_HEIGHT/2
DELAY = 0.025
colors = {0: 'red', 1: 'red', 2: 'orange', 3: 'orange', 4: 'yellow', 
         5: 'yellow', 6: 'green', 7: 'green', 8: 'cyan', 9: 'cyan'}

def main():
    canvas = graphics.Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    life = 3
    
    # 1. CREATE BRICKS
    num_rows = 10 
    num_cols = 10
    num_bricks = num_rows*num_cols
    bricks_remaining = canvas.create_text(350, 20, text='Bricks remaining '+str(num_bricks), font_size=15)
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * BRICK_WIDTH + col*BRICK_GAP
            top_y = row * BRICK_HEIGHT + row*BRICK_GAP + 50
            right_x = left_x + BRICK_WIDTH   # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = top_y + BRICK_HEIGHT   # The bottom coordinate of the cell is CELL_SIZE pixels away from the top
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, colors[row])
    
    paddle = canvas.create_rectangle(CANVAS_WIDTH-PADDLE_WIDTH/2, CANVAS_HEIGHT-20-PADDLE_HEIGHT,
                                     CANVAS_WIDTH+PADDLE_WIDTH/2, CANVAS_HEIGHT-20)
    
    # 2. ADD A BOUNCING BALLS
    x_velocity = change_x
    y_velocity = change_y
    ball_x = START_X
    ball_y = START_Y
    ball = canvas.create_oval(ball_x, ball_y,
                              ball_x + BALL_RADIUS*2,
                              ball_y + BALL_RADIUS*2,
                              'blue')
    
    while True:
        if (ball_x == 0) or (ball_x + BALL_RADIUS*2 >= CANVAS_WIDTH):
            x_velocity = -x_velocity
        if (ball_y == 0):
            y_velocity = -y_velocity
        ball_x += x_velocity
        ball_y += y_velocity
        canvas.moveto(ball, ball_x, ball_y)
        time.sleep(DELAY)
    # 3. ADD THE PADDLE
        mouse_x = canvas.get_mouse_x()
        canvas.moveto(paddle, mouse_x-PADDLE_WIDTH/2, CANVAS_HEIGHT-20-PADDLE_HEIGHT)
        
    # 4. CHECK FOR COLLISIONS
        x_1 = canvas.get_left_x(ball)
        y_1 = canvas.get_top_y(ball)
        x_2 = x_1 + 2*BALL_RADIUS
        y_2 = y_1 + 2*BALL_RADIUS
        colliding_list = canvas.find_overlapping(x_1, y_1, x_2, y_2)
        print(colliding_list)
        for object in colliding_list:
            if object == paddle:
                y_velocity = -y_velocity
            elif object != ball:
                canvas.delete(object)
                y_velocity = -y_velocity
                num_bricks -= 1
                canvas.delete(bricks_remaining)
                bricks_remaining = canvas.create_text(350, 20, text='Bricks remaining '+str(num_bricks), font_size=15)
                break
    
    # 5. PLAY THREE TURNS
        if ball_y + BALL_RADIUS*2 >= CANVAS_HEIGHT:
            life -= 1
            if life == 0:
                canvas.create_text(CANVAS_WIDTH/2-150, CANVAS_HEIGHT/2, text='GAME OVER!', font_size = 50)
                return
            else:
                ball_x = START_X
                ball_y = START_Y
                canvas.moveto(ball, ball_x, ball_y)
                
    # 6. HIT ALL BRICKS
        if num_bricks == 0:
            canvas.create_text(CANVAS_WIDTH/2-100, CANVAS_HEIGHT/2-50, text='YOU WIN!', font_size = 40)
            canvas.create_text(CANVAS_WIDTH/2-200, CANVAS_HEIGHT/2, text='CONGRATULATIONS', font_size = 40)
            return
        
if __name__ == '__main__':
    main()
