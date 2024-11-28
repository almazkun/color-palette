from ninja import NinjaAPI

from color.api import router

api = NinjaAPI()

api.add_router("/v1/", router)
