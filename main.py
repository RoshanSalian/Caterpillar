import random
import turtle as t

t.bgcolor('yellow')

cat = t.Turtle()
cat.shape('square')
cat.color('red')
cat.speed(0)
cat.penup()
cat.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)

leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_start = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to play', align='center', font=('Arial', 16, 'bold'))

text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = -(left_wall)

    top_wall =  t.window_height()/2
    bottom_wall = -t.window_height()/2

    (x, y) = cat.pos()
    outside = x < left_wall or x >right_wall or y < bottom_wall or y > top_wall

    return outside

def game_over():
    cat.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write("Game Over! Your Score -"+str(score), align = 'center',  font=('Arial', 30, 'normal'))


def display_score(score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 90
    score_turtle.setpos(x, y)
    score_turtle.write(str(score), align='right', font=('Arial', 40, 'bold'))


def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st() # Showturtle


def start_game():
    global game_started
    game_started = False
    if game_started:
        return

    game_started = True

    score = 0
    text_turtle.clear()

    cat_speed=2
    cat_length = 3
    cat.shapesize(1, cat_length, 1)
    cat.showturtle()
    display_score(score)
    place_leaf()

    while True:
        cat.forward(cat_speed)
        if cat.distance(leaf) < 20:
            place_leaf()
            cat_length += 1
            cat.shapesize(1, cat_length, 1)
            cat_speed += 1
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break


def move_up():
    if cat.heading() == 0 or cat.heading()==180:
        cat.setheading(90)


def move_down():
    if cat.heading() == 0 or cat.heading() == 180:
        cat.setheading(270)


def move_left():
    if cat.heading() == 90 or cat.heading() == 270:
        cat.setheading(180)


def move_right():
    if cat.heading() == 90 or cat.heading() == 270:
        cat.setheading(0)


t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')
t.listen()
t.mainloop()
