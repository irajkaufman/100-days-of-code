from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.dots = 0
        self.color(COLOR)
        self.up
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.dots}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def dot_tracker(self):
        self.dots += 1
        self.update_scoreboard()
