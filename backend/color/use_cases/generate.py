from random import randint
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


def swatches(color_space: str, count: int):
    if color_space not in color_generators:
        raise ValueError(f"Unsupported color space: {color_space}")
    return [color_generators[color_space]() for _ in range(count)]
