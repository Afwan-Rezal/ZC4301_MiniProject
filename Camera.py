import pygame
from OpenGL.GLU import *
from math import *


class Camera:
    def __init__(self):
        self.eye = pygame.math.Vector3(0, 0, 0)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.look = self.eye + self.forward

        self.yaw = -90
        self.pitch = 0
        self.last_mouse = pygame.math.Vector2(0, 0)

        self.mouse_sensitivityX = 1
        self.mouse_sensitivityY = 1
        self.movement_speed = 1
        self.movement_dampening = 0.8

        self.is_mouse_held = False
        self.mouse_delta_smoothing = pygame.math.Vector2(0, 0)

    def rotate(self, pitch, yaw):
        self.yaw += yaw
        self.pitch = max(-89.0, min(89.0, self.pitch + pitch))

        self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward.y = sin(radians(self.pitch))
        self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward = self.forward.normalize()

        self.right = self.forward.cross(pygame.Vector3(0, 1, 0)).normalize()
        self.up = self.right.cross(self.forward).normalize()

    def handle_mouse_movement(self):
        # Check if right mouse button is held down
        if pygame.mouse.get_pressed()[2]:  # Right mouse button is index 2
            # Only set `last_mouse` on initial right-click press
            if not self.is_mouse_held:
                self.is_mouse_held = True
                self.last_mouse = pygame.math.Vector2(pygame.mouse.get_pos())

            # Calculate mouse movement and apply smoothing
            mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
            mouse_delta = self.last_mouse - mouse_pos
            self.last_mouse = mouse_pos

            # Apply smoothing
            self.mouse_delta_smoothing += mouse_delta * 0.1
            mouse_delta = self.mouse_delta_smoothing * 0.8
            self.mouse_delta_smoothing *= 0.8

            # Rotate based on smoothed mouse delta (swapped x and y for correct orientation)
            self.rotate(mouse_delta.y * self.mouse_sensitivityY, -mouse_delta.x * self.mouse_sensitivityX)
        else:
            # Reset if the right mouse button is released
            self.is_mouse_held = False

    def handle_keyboard_input(self):
        keys = pygame.key.get_pressed()
        movement = pygame.math.Vector3(0, 0, 0)

        key_movement = {
            pygame.K_UP: self.forward,
            pygame.K_DOWN: -self.forward,
            pygame.K_LEFT: self.right,
            pygame.K_RIGHT: -self.right
        }

        for key, direction in key_movement.items():
            if keys[key]:
                movement += direction * self.movement_speed

        # Apply movement dampening for smoother transitions
        self.eye += movement * self.movement_dampening

    def update(self):
        self.handle_mouse_movement()
        self.handle_keyboard_input()
        self.look = self.eye + self.forward

        gluLookAt(
            self.eye.x, self.eye.y, self.eye.z,
            self.look.x, self.look.y, self.look.z,
            self.up.x, self.up.y, self.up.z
        )


