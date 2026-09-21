import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "INIT":

        if True:
            state = "DOWN_1"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    if state == "DOWN_1":
        t.forward(10)  # Движение

        if y <= -4:
            state = "RIGHT_1"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT_1":
        t.forward(10)  # Движение

        if x >= 4:
            state = "UP_1"
            t.setheading(90)  # Поворот вверх
            return state, turn
        return state, turn
    if state == "UP_1":
        t.forward(10)  # Движение

        if y >= 0:
            state = "LEFT_1"
            t.setheading(180)  # Поворот влево
            return state, turn
        return state, turn
    if state == "LEFT_1":
        t.forward(10)  # Движение

        if x <= 1:
            state = "DOWN_2"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    if state == "DOWN_2":
        t.forward(10)  # Движение

        if y <= -3:
            state = "RIGHT_2"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT_2":
        t.forward(10)  # Движение

        if x >= 3:
            state = "UP_2"
            t.setheading(90)  # Поворот вверх
            return state, turn
        return state, turn
    if state == "UP_2":
        t.forward(10)  # Движение

        if y >= -1:
            state = "LEFT_2"
            t.setheading(180)  # Поворот влево
            return state, turn
        return state, turn
    if state == "LEFT_2":
        t.forward(10)  # Движение

        if x <= 2:
            state = "DOWN_3"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    if state == "DOWN_3":
        t.forward(10)  # Движение

        if y <= -2:
            state = "STOP"
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()