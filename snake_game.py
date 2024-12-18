import turtle
import random
import time
delay = 0.1
#set up the screen
wn = turtle.Screen()
wn.bgcolor('lavender')
wn.title('Snake Game by MJ')
wn.setup(width=600,height=600)
wn.tracer(0)

#snake_head
head = turtle.Turtle()
head.shape('circle')
head.color('purple')
head.speed(0)
head.goto(0,0)
head.penup()
head.forward(100)
head.direction='Stop'
#snake food
food = turtle.Turtle()
food.shape('circle')
food.color('silver')
food.speed(0)
food.penup()
food.goto(random.randint(-290,290),random.randint(-290,290))

#score
score = 0
pen = turtle.Turtle()
pen.shape('circle')
pen.color('red')
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f'SCORE " {score}',align='right',font='arial')

def move():
    if head.direction == 'Up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'Down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'Right':
        x = head.xcor()
        head.setx(x+20)
    if head.direction == 'Left':
        x = head.xcor()
        head.setx(x-20)
def go_up():
    head.direction = 'Up'
def go_down():
    head.direction = 'Down'
def go_right():
    head.direction = 'Right'
def go_left():
    head.direction = 'Left'
wn.listen()
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_right,'Right')
wn.onkeypress(go_left,'Left')

body = []
while True:
    wn.update()
    if head.ycor()>290 or head.ycor()<-290\
       or head.xcor()>290 or head.xcor()<-290:
        head.goto(0,0)
        time.sleep(2)
        head.direction = 'Stop'
        score = 0
        pen.clear()
        pen.write(f'SCORE " {score}',align='right',font='arial')
        
        for new_body in body:
            new_body.goto(1000,1000)
        body.clear()
    if head.distance(food)<20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        score += 1
        pen.clear()
        pen.write(f'SCORE " {score}',align='right',font='arial')
        food.goto(x,y)
        new_body = turtle.Turtle()
        new_body.shape('circle')
        new_body.color('black')
        new_body.speed(0)
        new_body.penup()
        body.append(new_body)
        
    for i in range(len(body)-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)
            
    time.sleep(delay)
    move()
    
#Body colision
    for new_nody in body:
        if new_body.distance(head)<20:
            head.goto(0,0)
            time.sleep(2)
            head.direction = 'Stop'
            score = 0
            delay -= 0.1
            
            pen.clear()
            pen.write(f'SCORE " {score}',align='right',font='arial')
            for new_body in body:
                new_body.goto(1000,1000)
            body.clear()
wn.mainloop()