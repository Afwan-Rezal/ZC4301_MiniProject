from OpenGL.GL import *
import pygame
from .GraphicsData import GraphicsData
from .Uniform import *
import numpy as np


class Mesh:
    def __init__(self, program_id, vertices, vertex_colors, draw_type,
                 translation=pygame.Vector3(0, 0, 0)):
        self.vertices = vertices
        self.draw_type = draw_type
        self.vao_ref = glGenVertexArrays(1)

        glBindVertexArray(self.vao_ref)

        position = GraphicsData("vec3", self.vertices)
        position.create_variable(program_id, "position")

        colors = GraphicsData("vec3", vertex_colors)
        colors.create_variable(program_id, "vertex_color")

        self.translation = Uniform("vec3", translation)
        self.translation.find_variable(program_id, "translation")

    def draw(self):
        glBindVertexArray(self.vao_ref)
        self.translation.load()  # Ensure translation is loaded before drawing
        glDrawArrays(self.draw_type, 0, len(self.vertices))

