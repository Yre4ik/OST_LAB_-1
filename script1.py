import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "DOWN_4":
        t.forward(10)  # Движение

        if y<=-3:
            state = "RIGHT_3"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT_3":
        t.forward(10)  # Движение

        if x>=5:
            state = "STOP"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "UNIT":

        if True:
            state = "RIGHT_1"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT_1":
        t.forward(10)  # Движение

        if x>=5:
            state = "DOWN_1"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    if state == "DOWN_1":
        t.forward(10)  # Движение

        if y<=0:
            state = "LEFT_1"
            t.setheading(180)  # Поворот влево
            return state, turn
        return state, turn
    if state == "LEFT_1":
        t.forward(10)  # Движение

        if x<=1:
            state = "DOWN_2"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    if state == "DOWN_2":
        t.forward(10)  # Движение

        if y<=-1:
            state = "RIGHT_2"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT_2":
        t.forward(10)  # Движение

        if x>=5:
            state = "DOWN_3"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    if state == "DOWN_3":
        t.forward(10)  # Движение

        if y<=-2:
            state = "LEFT_2"
            t.setheading(180)  # Поворот влево
            return state, turn
        return state, turn
    if state == "LEFT_2":
        t.forward(10)  # Движение

        if x<=1:
            state = "DOWN_4"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "UNIT"
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