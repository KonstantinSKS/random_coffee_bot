import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tg_bot.config import (
    MEETING_DAY, MEETING_TIME, QUESTION_DAY, QUESTION_TIME)
from tg_bot.loader import bot, dp
from tg_bot.misc.creating_unique_pairs import start_random_cofee
from tg_bot.misc.mailing import mailing_date, mailing_question
from tg_bot.misc.utils import set_commands


async def main():
    logging.info('Начало работы бота.')
    await set_commands(bot)
    scheduler = AsyncIOScheduler()

    # еженедельная рассылка встреч
    scheduler.add_job(
        start_random_cofee,
        trigger='cron',
        day_of_week=MEETING_DAY,
        hour=MEETING_TIME,
    )

    # еженедельная рассылка вопроса о проведенной встречи
    scheduler.add_job(
        mailing_question,
        trigger='cron',
        day_of_week=QUESTION_DAY,
        hour=QUESTION_TIME,
    )

    # проверка наличия рассылки
    scheduler.add_job(
        mailing_date,
        trigger='interval',
        minutes=1,
    )

    scheduler.start()
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
