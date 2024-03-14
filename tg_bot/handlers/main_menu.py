from aiogram import Router, F
from aiogram.types import Message

main_menu_router = Router()

MSG_SUSPEND = (
    'Если вы передумали принимать участие в какую-либо неделю или '
    'уходите в отпуск, то можно приостановить участие в проекте.'
)
MSG_REVIEW = (
    '<b>Милена Мелкова, Cпециалист по продукту.</b>'
    '\n«Кофе вслепую» - отличная возможность познакомиться с коллегами '
    'из других отделов, в том числе с менеждерами и Директорами, которые '
    'тоже участвуют в проекте.'
    '\n'
    '\n<b>Анастасия Родкина, Младший менеджер по работе с ключевыми '
    'клиентами.</b>'
    '\nКрутая возможность пообщаться, лучше узнать новых сотрудников, '
    'наладить неформальный контакт в условиях удаленной работы… '
    'Поделиться своим опытом и получить заряд позитива! В крупных '
    'компаниях как наша - это необходимо! Спасибо за классный проект!'
    '\n'
    '\n<b>Анна Борисевич, Старший специалист по цифровому контенту.</b>'
    '\nМне безумно нравится эта инициатива! Уникальная возможность '
    'быстро познакомиться с коллегами, узнать что-то новое и зарядиться '
    'позитивной энергией на весь день 🤩Всем новичкам и бывалым искренне '
    'советую попробовать поучаствовать и получить приятные впечатления 🥰'
)


@main_menu_router.message(F.text == 'Приостановить участие')
async def suspend_participation(message: Message):
    """Приостановление участия."""
    await message.answer(MSG_SUSPEND)


@main_menu_router.message(F.text == 'Наши коллеги про проект «Кофе вслепую»')
async def reviews(message: Message):
    """Сообщение о проекте."""
    await message.answer(MSG_REVIEW)
