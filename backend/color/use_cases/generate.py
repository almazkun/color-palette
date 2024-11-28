from random import choice, randint
from typing import Any, Callable, Dict

color_generators: Dict[str, Callable[[], Dict[str, Any]]] = {}


def register_color_space(color_space: str, generator: Callable[[], Dict[str, Any]]):
    color_generators[color_space] = generator


def generate_rgb():
    return {
        "color_space": "rgb",
        "r": randint(0, 255),
        "g": randint(0, 255),
        "b": randint(0, 255),
    }


def generate_hsl():
    return {
        "color_space": "hsl",
        "h": randint(0, 360),
        "s": randint(0, 100),
        "l": randint(0, 100),
    }


register_color_space("rgb", generate_rgb)
register_color_space("hsl", generate_hsl)


def swatches(count: int):
    color_spaces = [choice(list(color_generators.keys())) for _ in range(count)]
    return [color_generators[color_space]() for color_space in color_spaces]
