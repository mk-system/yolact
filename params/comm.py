# Parameters by calculating
from . import env
from . import image
from . import car

SCALE_RATIO = image.INPUT_IMAGE_WIDTH_PIXEL / env.WORLD_WIDTH_MM
SCALE_CAR_LENGTH =  car.CAR_LENGTH_MM * SCALE_RATIO
SCALE_CAR_WIDTH =  car.CAR_WIDTH_MM * SCALE_RATIO
