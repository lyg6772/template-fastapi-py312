from app.controller.hello import hello_get_controller
from fastapi import APIRouter

router = APIRouter()

router.add_api_route("/hello", hello_get_controller, methods=["get"])
