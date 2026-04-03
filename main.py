from src.simulation import Simulation
from src.vision import detect_obstacles, get_obstacle_density
from src.decision import decide_movement

import pygame
import cv2

def main():
    sim = Simulation()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # frame dalla simulazione
        frame = sim.get_frame()

        # Visione
        edges = detect_obstacles(frame)
        density = get_obstacle_density(edges)

        # Decisione
        action = decide_movement(density)

        # Movimento
        sim.move_robot(action)

        # Disegno
        sim.draw()
        sim.tick()

        # Debug 
        cv2.imshow("Vision", edges)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    pygame.quit()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
