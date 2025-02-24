import aiomysql
from app import config

DB_CONFIG = {
    "host": config.DB_HOST,
    "password": config.DB_PW,
    "db": config.DB_DB,
    "user": config.DB_USER,
    "port": config.DB_PORT,
}


# 커넥션 풀 설정
async def init_db_pool():
    pool = await aiomysql.create_pool(
        minsize=1, maxsize=3, **DB_CONFIG  # 최소 커넥션 수  # 최대 커넥션 수
    )
    return pool
