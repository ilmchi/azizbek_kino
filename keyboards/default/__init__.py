from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu.add(
    KeyboardButton("🎬 Kino qo‘shish"),
    KeyboardButton("🗑 Kino o‘chirish")
).add(
    KeyboardButton("🔍 Qidirish (Caption)"),
    KeyboardButton("🔎 Qidirish (ID)")
).add(
    KeyboardButton("♻️ Kino update qilish"),
    KeyboardButton("📊 Statistika")
).add(
    KeyboardButton("📤 Reklama yuborish")
)
