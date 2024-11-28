import logging

from ninja import Router
from ninja.errors import ValidationError

from color.schemas import SwatchOutput
from color.use_cases import generate

logger = logging.getLogger(__name__)
router = Router()


class SwatchRequestException(ValidationError):
    pass


@router.get("/swatches/", response=SwatchOutput)
def get_swatches(request):
    try:
        return {"swatches": generate.swatches(5)}
    except Exception as e:
        logger.exception(".get_swatches: Error generating swatches")
        raise SwatchRequestException(
            errors=[
                {
                    "loc": ["path", "color_space"],
                    "msg": "Unexpected error generating swatches",
                    "type": e.__class__.__name__,
                }
            ]
        ) from e
