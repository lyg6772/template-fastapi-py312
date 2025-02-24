from fastapi import Request

# from app.service.hello import HelloService


async def hello_get_controller(requests: Request):
    return "hello"


# async def hello_db_controller(requests: Request):
#     return async await
