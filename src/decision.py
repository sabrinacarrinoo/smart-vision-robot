def decide_movement(obstacle_density):
    """
    Decide movimento del robot
    """

    if obstacle_density > 40:
        return "LEFT"
    elif obstacle_density > 20:
        return "RIGHT"
    else:
        return "FORWARD"
