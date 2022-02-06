from turtle import Turtle, Screen
import heroes

class Snake:

    def __init__(self):
        self.create_snake()



    def create_snake(self):
        self.snake_names = heroes.genarr(3)
        y = 0
        for i in range(len(self.snake_names)):
            x = 0 - (20 * i)
            self.snake_names[i] = Turtle("square")
            self.snake_names[i].penup()
            self.snake_names[i].color("white")
            self.snake_names[i].setposition(x, y)
        self.head = self.snake_names[0]

    def move(self):
        for n in range(len(self.snake_names) - 1, 0, -1):
            positionx = self.snake_names[n-1].xcor()
            positiony = self.snake_names[n - 1].ycor()
            self.snake_names[n].goto(positionx, positiony)
        # screen.onkeypress(key="d", fun=snake_names[0].right(90))
        self.snake_names[0].forward(20)



    def right(self):
        if self.snake_names[0].heading() != 180:
            self.snake_names[0].setheading(0)


    def left(self):
        if self.snake_names[0].heading() != 0:
            self.snake_names[0].setheading(180)

    def up(self):
        if self.snake_names[0].heading() != 270:
            self.snake_names[0].setheading(90)

    def down(self):
        if self.snake_names[0].heading() != 90:
            self.snake_names[0].setheading(270)


    def score(self):
        self.snake_names.append(heroes.gen())
        self.snake_names[len(self.snake_names)-1] = Turtle("square")
        self.snake_names[len(self.snake_names)-1].penup()
        self.snake_names[len(self.snake_names)-1].color("white")
        positionx = self.snake_names[len(self.snake_names)-2].xcor()
        positiony = self.snake_names[len(self.snake_names)-2].ycor()
        self.snake_names[len(self.snake_names)-1].goto(positionx, positiony)

    def colision_detection(self):
        for x in self.snake_names[3: ]:
            if self.head.distance(x) < 5:
                return True


    def reset(self):
        for seg in self.snake_names:
            seg.goto(1000, 1000)
        self.snake_names.clear()

        self.create_snake()
        self.head = self.snake_names[0]