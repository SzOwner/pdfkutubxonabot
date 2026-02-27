from db import get_db

ROLE_LEVEL = {
    "moderator": 1,
    "admin": 2,
    "superadmin": 3
}

async def get_role(user_id: int):
    db = await get_db()
    cur = await db.execute("SELECT role FROM roles WHERE user_id=?", (user_id,))
    row = await cur.fetchone()
    await db.close()
    return row[0] if row else None

async def has_permission(user_id: int, min_role: str):
    role = await get_role(user_id)
    return ROLE_LEVEL.get(role, 0) >= ROLE_LEVEL.get(min_role, 0)