from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()
        self.hideturtle()
    
    def update(self):
        self.write(f"Score: {self.score}",font=("Courier", 18, "bold"), align="center")
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 18, "bold"))
    
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()

    def increase_higher(self):
        self.score+=10
        self.clear()
        self.update()



# from turtle import Turtle

# class Scoreboard(Turtle):
#     def init(self):
#         super().init()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#         self.update()
#         self.hideturtle()

#     def update(self):
#         self.clear()
#         self.write(f"Score: {self.score}", font=("Courier", 18, "bold"), align="center")

#     def game_over(self):
#         self.goto(0, 0)
#         self.write("GAME OVER", align="center", font=("Courier", 18, "bold"))

#     def increase_score(self):
#         self.score += 1
#         self.update()

#     def increase_higher(self):
#         self.score += 10
#         self.update()

