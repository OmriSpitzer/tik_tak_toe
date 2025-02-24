from abc import ABC, abstractmethod
import pygame
import color as cl


class Shape(ABC, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    @abstractmethod
    def draw(self, surface, x, y):
        pass


class Square(Shape):
    def __init__(self, width, color=cl.Color.BLACK, inner_color=cl.Color.WHITE, border=2):
        super().__init__()

        self._width = width
        self._color = color.value
        self._inner_color = inner_color.value
        self._border = border

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, self._color, (x, y, self._width, self._width))
        pygame.draw.rect(surface, self._inner_color, (x + self._border, y + self._border,
                                                      self._width - 2 * self._border, self._width - 2 * self._border))


class Circle(Shape):
    def __init__(self, radius, color=cl.Color.BLACK, inner_color=cl.Color.WHITE, border=2):
        super().__init__()

        self._radius = radius
        self._color = color.value
        self._inner_color = inner_color.value
        self._border = border

    def draw(self, surface, x, y):
        pygame.draw.circle(surface, self._color, (x+self._radius, y+self._radius), self._radius)
        pygame.draw.circle(surface, self._inner_color, (x+self._radius, y+self._radius), self._radius - self._border)


class Cross(Shape):
    def __init__(self, length, color=cl.Color.BLACK, border=4):
        super().__init__()
        self._length = length
        self._color = color.value
        self._border = border

    def draw(self, surface, x, y):
        pygame.draw.line(surface, self._color, (x, y), (x + self._length, y + self._length), self._border)
        pygame.draw.line(surface, self._color, (x, y + self._length), (x + self._length, y), self._border)
