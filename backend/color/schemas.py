from enum import Enum
from typing import List, Union

from ninja import Field, Schema


class ColorSpace(str, Enum):
    RGB = "rgb"
    HSL = "hsl"
    HEX = "hex"


class BaseColor(Schema):
    color_space: ColorSpace


class RGBColor(BaseColor):
    r: int = Field(..., ge=0, le=255, description="Red value (0-255)")
    g: int = Field(..., ge=0, le=255, description="Green value (0-255)")
    b: int = Field(..., ge=0, le=255, description="Blue value (0-255)")


class HSLColor(BaseColor):
    h: int = Field(..., ge=0, le=360, description="Hue value (0-360)")
    s: int = Field(..., ge=0, le=100, description="Saturation value (0-100)")
    l: int = Field(..., ge=0, le=100, description="Lightness value (0-100)")


class HEXColor(BaseColor):
    hex: str = Field(..., description="Hex value")


class SwatchOutput(Schema):
    swatches: List[Union[RGBColor, HSLColor, HEXColor]]
