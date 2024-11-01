import argparse
import logging
import os

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import UserPrivacyRestrictedError
from telethon.tl.functions.messages import AddChatUserRequest

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
GROUP_ID = int(os.getenv("GROUP_ID"))


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


async def add_users_to_group(client, user_ids):
    for user_id in user_ids:
        try:
            await client(AddChatUserRequest(
                chat_id=GROUP_ID,
                user_id=user_id,
                fwd_limit=100
            ))
        except UserPrivacyRestrictedError:
            logger.exception(f"Пользователь {user_id} не может быть добавлен из-за настроек приватности.", exc_info=True)
        except Exception as e:
            logger.exception(f"Ошибка при добавлении пользователя {user_id}: {e}", exc_info=True)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        help="TXT file with user_ids to invite; example: 1234\\n12345...",
        required=True
    )
    args = parser.parse_args()

    with open(args.file, "r") as f:
        users = [int(u.rstrip()) for u in f.readlines() if u.rstrip()]

    async with TelegramClient("session", API_ID, API_HASH) as client:
        await add_users_to_group(client, users)
        await client.disconnect()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
