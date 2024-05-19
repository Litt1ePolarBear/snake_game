from turtle import Turtle
ALIGN = ("center")
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.py") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} / High score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.py", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
