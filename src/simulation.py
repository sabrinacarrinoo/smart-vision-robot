import pygame
import random

WIDTH, HEIGHT = 600, 600
ROBOT_SIZE = 20
OBSTACLE_SIZE = 40

class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Smart Robot Simulation")

        self.robot_x = WIDTH // 2
        self.robot_y = HEIGHT - 50

        self.obstacles = []
        self.clock = pygame.time.Clock()

        self.spawn_obstacles()

    def spawn_obstacles(self):
        for _ in range(5):
            x = random.randint(0, WIDTH - OBSTACLE_SIZE)
            y = random.randint(0, HEIGHT // 2)
            self.obstacles.append(pygame.Rect(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE))

    def move_robot(self, direction):
        if direction == "LEFT":
            self.robot_x -= 5
        elif direction == "RIGHT":
            self.robot_x += 5
        elif direction == "FORWARD":
            self.robot_y -= 5

    def draw(self):
        self.screen.fill((0, 0, 0))

        # Robot
        pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            (self.robot_x, self.robot_y, ROBOT_SIZE, ROBOT_SIZE),
        )

        # Ostacoli
        for obs in self.obstacles:
            pygame.draw.rect(self.screen, (255, 0, 0), obs)

        pygame.display.flip()

    def get_frame(self):
        """
        Converte schermata pygame in immagine OpenCV
        """
        frame = pygame.surfarray.array3d(self.screen)
        frame = frame.swapaxes(0, 1)
        return frame

    def tick(self):
        self.clock.tick(30)
