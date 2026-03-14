"""
╔══════════════════════════════════════════════╗
║        🌿 ECOBALA TELEGRAM BOT               ║
║        Написан на aiogram 3.x                ║
║                                              ║
║  Установка:                                  ║
║    pip install aiogram                       ║
║                                              ║
║  Запуск:                                     ║
║    python ecobala_bot.py                     ║
╚══════════════════════════════════════════════╝
"""

import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# ═══════════════════════════════════════════════════
#  ⚙️  НАСТРОЙКИ — заменить на свои!
# ═══════════════════════════════════════════════════
BOT_TOKEN    = "8508126262:AAHeQr0ppPwrs1AjJYr0_Ouqm_6_rGI_Wt0"
MINI_APP_URL = "https://ecobalakz.netlify.app/"

PHONE     = "+7 705 962 8198"
WA_LINK   = "https://wa.me/77059628198"
INSTAGRAM = "https://instagram.com/ecobala.kz"
YOUTUBE   = "https://youtube.com/channel/UCfkYVJYXBwAlhz5vK8VACKA"
# ═══════════════════════════════════════════════════

logging.basicConfig(level=logging.INFO)


# ───────────────────────────────────────────────────
#  📋 ТЕКСТЫ
# ───────────────────────────────────────────────────
TEXT_MAIN = (
    "🌿 *EcoBala — Экологический проект Казахстана*\n\n"
    "Привет\\! Мы помогаем людям и бизнесу жить осознанно "
    "и заботиться о природе 🇰🇿\n\n"
    "Выберите раздел ниже 👇"
)

TEXT_ABOUT = (
    "🌿 *О проекте EcoBala*\n\n"
    "*EcoBala* — казахстанский экологический проект, созданный с одной целью: "
    "сделать планету чище, а жизнь людей — осознаннее\\.\n\n"
    "🎯 *Наша миссия*\n"
    "Формировать экологическую культуру в Казахстане через образование и совместные действия\\.\n\n"
    "♻️ *Что мы делаем:*\n"
    "• Организуем раздельный сбор отходов\n"
    "• Проводим эко\\-уроки и мастер\\-классы\n"
    "• Партнёрствуем с бизнесом и школами\n"
    "• Создаём эко\\-контент\n"
    "• Участвуем в экологических акциях\n\n"
    "💚 Каждый шаг важен\\!"
)

TEXT_SERVICES = (
    "🛠️ *Наши услуги*\n\n"
    "🏢 *Для бизнеса:*\n"
    "• Организация раздельного сбора на предприятии\n"
    "• Эко\\-аудит офиса и производства\n"
    "• Корпоративные эко\\-тренинги\n"
    "• Эко\\-брендинг и партнёрство\n\n"
    "🏫 *Для школ и вузов:*\n"
    "• Эко\\-уроки и интерактивные лекции\n"
    "• Организация субботников\n"
    "• Конкурсы и квесты для детей\n\n"
    "🌍 *Для НКО и государства:*\n"
    "• Партнёрство в экологических проектах\n"
    "• Совместные акции\n\n"
    "📩 Напишите нам для консультации\\!"
)

TEXT_CONTACTS = (
    "📞 *Контакты EcoBala*\n\n"
    "Мы всегда рады сотрудничеству\\!\n\n"
    "📸 *Instagram:* [ecobala\\.kz](https://instagram.com/ecobala.kz)\n\n"
    "▶️ *YouTube:* [EcoBala Channel](https://youtube.com/channel/UCfkYVJYXBwAlhz5vK8VACKA)\n\n"
    "Пишите — ответим быстро\\! 🌿"
)

TEXT_JOIN = (
    "💚 *Присоединяйтесь к EcoBala\\!*\n\n"
    "Стань частью экологического движения Казахстана 🇰🇿\n\n"
    "👤 *Как можно участвовать:*\n"
    "• Волонтёр на эко\\-акциях\n"
    "• Эко\\-амбассадор в своём городе\n"
    "• Партнёр проекта\n"
    "• Спонсор или донор\n\n"
    "🌱 Вместе мы можем изменить мир\\!\n"
    "Напишите нам — ответим в течение 24 часов\\."
)


# ───────────────────────────────────────────────────
#  ⌨️  КЛАВИАТУРЫ
# ───────────────────────────────────────────────────
def kb_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌿 О проекте",   callback_data="about")],
        [
            InlineKeyboardButton(text="🛠 Услуги",    callback_data="services"),
            InlineKeyboardButton(text="💚 Вступить",  callback_data="join"),
        ],
        [InlineKeyboardButton(text="📞 Контакты",    callback_data="contacts")],
        [InlineKeyboardButton(
            text="📱 Открыть EcoApp",
            web_app=WebAppInfo(url=MINI_APP_URL),
        )],
        [
            InlineKeyboardButton(text="📸 Instagram", url=INSTAGRAM),
            InlineKeyboardButton(text="▶️ YouTube",   url=YOUTUBE),
        ],
    ])


def kb_back() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Главное меню",        callback_data="main")],
    ])


def kb_contacts() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 WhatsApp",    url=WA_LINK)],
        [
            InlineKeyboardButton(text="📸 Instagram", url=INSTAGRAM),
            InlineKeyboardButton(text="▶️ YouTube",   url=YOUTUBE),
        ],
        [InlineKeyboardButton(text="◀️ Главное меню", callback_data="main")],
    ])


# ───────────────────────────────────────────────────
#  🤖 КОМАНДЫ
# ───────────────────────────────────────────────────
async def cmd_start(message: Message):
    name = message.from_user.first_name or "друг"
    await message.answer(
        f"Привет, *{name}*\\! 👋\n\n" + TEXT_MAIN,
        reply_markup=kb_main(),
    )


async def cmd_about(message: Message):
    await message.answer(TEXT_ABOUT, reply_markup=kb_back())


async def cmd_services(message: Message):
    await message.answer(TEXT_SERVICES, reply_markup=kb_back())


async def cmd_contacts(message: Message):
    await message.answer(
        TEXT_CONTACTS,
        reply_markup=kb_contacts(),
        disable_web_page_preview=True,
    )


async def cmd_join(message: Message):
    await message.answer(TEXT_JOIN, reply_markup=kb_back())


async def any_message(message: Message):
    await message.answer(TEXT_MAIN, reply_markup=kb_main())


# ───────────────────────────────────────────────────
#  🖱️  КНОПКИ (callback)
# ───────────────────────────────────────────────────
async def cb_handler(callback: CallbackQuery):
    data = callback.data
    if data == "main":
        await callback.message.edit_text(TEXT_MAIN, reply_markup=kb_main())
    elif data == "about":
        await callback.message.edit_text(TEXT_ABOUT, reply_markup=kb_back())
    elif data == "services":
        await callback.message.edit_text(TEXT_SERVICES, reply_markup=kb_back())
    elif data == "contacts":
        await callback.message.edit_text(
            TEXT_CONTACTS,
            reply_markup=kb_contacts(),
            disable_web_page_preview=True,
        )
    elif data == "join":
        await callback.message.edit_text(TEXT_JOIN, reply_markup=kb_back())
    await callback.answer()


# ───────────────────────────────────────────────────
#  🚀 ЗАПУСК
# ───────────────────────────────────────────────────
async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
    )
    dp = Dispatcher()

    # Команды
    dp.message.register(cmd_start,    CommandStart())
    dp.message.register(cmd_about,    Command("about"))
    dp.message.register(cmd_services, Command("services"))
    dp.message.register(cmd_contacts, Command("contacts"))
    dp.message.register(cmd_join,     Command("join"))
    dp.message.register(any_message,  F.text)

    # Inline кнопки
    dp.callback_query.register(cb_handler, F.data.in_({"main","about","services","contacts","join"}))

    print("🌿 EcoBala Bot запущен! Ctrl+C для остановки.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())