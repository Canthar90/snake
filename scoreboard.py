from turtle import Turtle
ALLINGMENT ="center"
FONT = ('Gothic', 15, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.draw_score()

    def scoreup(self):
        self.score += 1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALLINGMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.draw_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", move=False, align=ALLINGMENT, font=FONT)




