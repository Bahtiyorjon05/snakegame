def play_game():
       
    from turtle import Screen
    from Snake import Snake
    from Food import Food
    from Food import SpecialFood
    from Scoreboard import Scoreboard
    import time

    screen = Screen()
    screen.bgcolor("black")
    difficulty=screen.textinput("Snake game", "Choose your level: 1, 2, 3, 4, 5")
    if difficulty not in ["1", "2", "3", "4", "5"]:
      screen.bye()
      return
    speed_map = {"1": 0.3, "2": 0.2, "3": 0.1, "4": 0.09, "5": 0.05}
    speed = speed_map[difficulty]
    screen.setup(width=800, height=600)
    screen.title("My Snake Game")
    screen.tracer(0)
    snake = Snake()
    food=Food()
    special_food=SpecialFood()
    scoreboard=Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(speed)
        snake.move()
        #Detect collision with food
        if snake.head.distance(food) <20:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

            # Detect with larger special food 

        if snake.head.distance(special_food) < 30 and special_food.isvisible():
            special_food.refresh()
            snake.extend()
            scoreboard.increase_higher()
        # Detect collision with wall
            
        if snake.head.xcor()> 390 or snake.head.xcor() < -400 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on=False
            scoreboard.game_over()
        
        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                    game_is_on=False
                    scoreboard.game_over()
        if game_is_on == False:
            answer=screen.textinput("Snake game", "Do you want to play again? Yes or No").lower()
            if answer=="yes":
                screen.reset()
                play_game()
    screen.exitonclick()
play_game()

        

        
