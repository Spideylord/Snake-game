from turtle import Turtle


class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.hits = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.file = open("Data.txt")
        self.high_score = int(self.file.read())
        self.file.close()
        self.goto(0,280)
        self.write(f"score:{self.hits} high score:{self.high_score}",False , "center" , ("Arial",15,"normal"))

    def interacted(self):
        self.hits += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.hits} high score:{self.high_score}", False, "center", ("Arial", 15, "normal"))


    def refresh(self):
        if self.hits > self.high_score :
            with open("Data.txt", "w") as file :
                file.write(f"{self.hits}")
            self.high_score = self.hits
        self.hits = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER !",False , "center" , ("Arial",15,"normal"))
