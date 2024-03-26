import aiohttp
from django.db import models

from tg_bot.config import BOT_TOKEN


class TgUser(models.Model):
    """Модель пользователя"""
    id = models.BigIntegerField(
        verbose_name='ID пользователя в Telegram', primary_key=True)
    email = models.EmailField(verbose_name='Почта', unique=True)
    enter_full_name = models.CharField(
        verbose_name='Введенное пользователем имя и фамилия',
        max_length=100,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=32,
        null=True,
        blank=True
    )
    full_name = models.CharField(verbose_name='Полное имя', max_length=100)
    bot_unblocked = models.BooleanField(
        verbose_name='Бот разблокирован пользователем', default=True)
    is_unblocked = models.BooleanField(
        verbose_name='Пользователь разблокирован', default=True)
    is_admin = models.BooleanField(
        verbose_name='Права администратора', default=False)
    is_active = models.BooleanField(
        verbose_name='Пользователь активен', default=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.id} {self.enter_full_name}'


class Meeting(models.Model):
    """Модель встречи"""
    user = models.ForeignKey(
        TgUser,
        on_delete=models.CASCADE,
        related_name='user_meetings',
        verbose_name='Пользователь',
    )
    partner = models.ForeignKey(
        TgUser,
        on_delete=models.CASCADE,
        related_name='partner_meetings',
        verbose_name='Партнёр',
    )
    date = models.DateField(
        verbose_name='Дата встречи',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'


class Mailing(models.Model):
    """Модель рассылки"""
    text = models.TextField(
        verbose_name='Текст рассылки',
        help_text='Введите текст рассылки',
        max_length=4096,
    )
    date_mailing = models.DateTimeField(
        verbose_name='Дата и время рассылки',
        help_text='Установите дату и время рассылки',
    )
    is_sent = models.BooleanField(
        verbose_name='Статус отправки',
        default=False,
    )

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


async def send_telegram_message(chat_id, text, token):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    async with aiohttp.ClientSession() as session:
        async with session.post(
                url,
                data={"chat_id": chat_id, "text": text}
        ) as response:
            return await response.text()


async def check_and_send_message_before_save(tg_user):
    chat_id = tg_user.id
    message_text = ('Вас разблокировал администратор'
                    if tg_user.is_unblocked else
                    'Вас заблокировал администратор')
    await send_telegram_message(chat_id, message_text, BOT_TOKEN)
