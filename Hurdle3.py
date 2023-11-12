def turn_right():
    turn_left()
    turn_left()
    turn_left()

def lewat_tembok():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while (not at_goal()):
    if wall_in_front():
        lewat_tembok()
    elif front_is_clear():
        move()
