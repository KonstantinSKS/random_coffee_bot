from aiogram import Router, F
from aiogram.types import Message


main_menu_router = Router()

ABOUT_TEXT = '''
В нашей компании есть прекрасная традиция знакомиться за чашечкой горячего кофе в Microsoft Teams или в офисе.
Раз в неделю будет автоматически приходить имя и фамилия коллеги в этот чат-бот, вам остается договориться
о дате и времени встречи в удобном для вас формате.
«Кофе вслепую»- это всегда:
    - Прекрасная компания;
    - Приятный и неожиданный сюрприз;
    - Помощь новым коллегам в адаптации;
    - Новые знакомства.
''' # noqa


@main_menu_router.message(F.text == 'О проекте')
async def about_project(message: Message):
    """ Раздел о проекте """
    await message.answer(ABOUT_TEXT)
