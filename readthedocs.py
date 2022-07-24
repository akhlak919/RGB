from manim import *
import numpy as np
import matplotlib.pyplot as plt
import math


class Candy(Scene):
    def construct(self):
        colors = [BLUE, PINK, GREEN, PURE_RED, YELLOW_D, WHITE, PURE_GREEN, ORANGE]
        text = Text("Shanghai is the Economic crisis.")
        text.set_color_by_gradient(BLUE, RED, GREEN_E, WHITE, ORANGE)
        self.add(text)
  
        text2 = Text("Hey Yup You are annoying").set_color(DARK_BLUE)
        text2.next_to(text, DOWN)

        math  = MathTex(r"\int_{0}^{\frac{\pi}{2}}\sin(\theta  + \beta) = \sin\theta\cos\beta + cos\theta\sin\beta")
        math.next_to(text, UP)
        math.set_color_by_gradient(colors)

        amber_heard = Text("Clause is mine time resin to amber heard.")
        amber_heard.next_to(text2, DOWN)
        self.add(amber_heard)

        self.add(text2, math)

        line = Line3D()

        self.add(line)

class Oracle(Scene):
    def construct(self):
        text = Text("Let\'s start with another example called for loop\n"
        "chaotic behaviour and it is a cinemmatic kind of insaniatiy").scale(0.676)
        text.set_color(PURE_BLUE)
        text.add_background_rectangle()
        text.get_center()
        self.add(text)   