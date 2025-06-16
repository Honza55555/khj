import os
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token from environment variable
API_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not API_TOKEN:
    logger.error("Please set the TELEGRAM_TOKEN environment variable")
    exit(1)

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# ====== Texts ======

CZ_MENU = """
🥐 <b>COFFEE PERK MENU</b> ☕️
U nás nejde jen o kafe. Je to malý rituál. Je to nálada. Je to... láska v šálku. 💘

☕ Výběrová káva  
🍳 Snídaně (lehké i pořádné)  
🍰 Domácí dorty  
🥗 Brunch a saláty

📄 <b>Kompletní menu:</b>
<a href="https://www.coffeeperk.cz/jidelni-listek">coffeeperk.cz/jidelni-listek</a>

Ať už si dáte espresso, matchu nebo zázvorovku – tady to chutná líp. 💛
"""

CZ_HOURS = """
🕐 <b>KDY MÁME OTEVŘENO?</b>

📅 <b>Pondělí–Pátek:</b> 7:30 – 17:00  
📅 <b>Sobota & Neděle:</b> ZAVŘENO

Chcete nás navštívit? Jsme tu každý všední den od brzkého rána.  
Těšíme se na vás! ☕
"""

CZ_WHERE = """
📍 <b>KDE NÁS NAJDETE?</b>

🏠 Vyskočilova 1100/2, Praha 4  
🗺️ <a href="https://goo.gl/maps/XU3nYKDcCmC2">Mapa</a>

Najdete nás snadno – stylová kavárna, příjemná atmosféra a lidé, co kávu berou vážně i s úsměvem.  
Zastavte se. Na chvilku nebo na celý den.
"""

CZ_CONTACT = """
📞 <b>KONTAKTUJTE NÁS</b>

📬 E-mail: info@coffeeperk.cz  
📞 Telefon: +420 725 422 518

Rádi vám pomůžeme s rezervací, odpovíme na vaše dotazy nebo poradíme s výběrem.  
Neváhejte se nám ozvat – jsme tu pro vás.
"""

CZ_PREORDER = """
📦 <b>PŘEDOBJEDNÁVKY</b>

Brzy spustíme možnost objednat si kávu a snídani předem přes Telegram.  
Zatím nás navštivte osobně – těšíme se! ☕️
"""

CZ_REASONS = """
😎 <b>DŮVODY, PROČ SI ZAJÍT NA KÁVU</b>

☕ Protože svět se lépe řeší s kofeinem.  
📚 Protože práce počká – espresso ne.  
💬 Protože dobrá konverzace začíná u šálku.  
👀 Protože dnes jste už skoro byli produktivní.  
🧠 Protože mozek startuje až po druhé kávě.  
🌦️ Protože venku prší... nebo svítí slunce... nebo prostě cítíte, že je čas.

A někdy netřeba důvod. Prostě jen přijďte. 💛
"""

EN_MENU = """
🥐 <b>COFFEE PERK MENU</b> ☕️
Coffee isn’t just a drink. It’s a ritual. A vibe. Love in a cup. 💘

☕ Specialty coffee to wake you up in the morning—and keep you sharp all day.  
🍳 Breakfast options—light bites or hearty feasts, depending on whether you’re surviving or conquering the day.  
🍰 Homemade cakes—for celebrations, breakups, or just because you deserve it.  
🥗 Brunch & salads—yes, we have something healthy that actually tastes good!

📄 <b>Full menu:</b>
<a href="https://www.coffeeperk.cz/jidelni-listek">coffeeperk.cz/jidelni-listek</a>

Whether it’s an espresso, matcha, or ginger latte—you’ll taste the difference. 💛
"""

EN_HOURS = """
🕐 <b>OPENING HOURS</b>

📅 <b>Mon–Fri:</b> 7:30 – 17:00  
📅 <b>Sat & Sun:</b> CLOSED (we’re recharging... or testing new pastries 🍰)

If you need your caffeine fix, we’re open early on weekdays.  
Can’t wait to see you! ☕
"""

EN_WHERE = """
📍 <b>FIND US AT</b>

🏠 Vyskočilova 1100/2, Prague 4  
🗺️ <a href="https://goo.gl/maps/XU3nYKDcCmC2">Map</a>

Look for the stylish café with great atmosphere and smiling people who take their coffee seriously.  
Drop by—whether for a quick break or a whole day’s work.
"""

EN_CONTACT = """
📞 <b>CONTACT & RESERVATIONS</b>

📬 Email: info@coffeeperk.cz  
📞 Phone: +420 725 422 518

We’re happy to help with reservations, answer questions, or guide you through our offerings.  
Feel free to reach out—we’re here for you.
"""

EN_PREORDER = """
📦 <b>PRE-ORDERS (COMING SOON)</b>

Soon you’ll be able to pre-order coffee and breakfast right here on Telegram.  
For now, visit us in person—we can’t wait! ☕️
"""

EN_REASONS = """
😎 <b>REASONS TO GRAB A COFFEE</b>

☕ Because the world runs on caffeine.  
📚 Because work can wait; espresso can’t.  
💬 Because good conversations start with coffee.  
👀 Because you were *almost* productive today.  
🧠 Because your brain boots after the second cup.  
🌦️ Because it’s raining... or sunny... or you just feel like it.

And sometimes, no reason is needed. Just come by. 💛
"""

# ====== Keyboards ======

# Language selection keyboard
lang_kb = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("🇨🇿 Čeština", callback_data="lang_cz"),
    InlineKeyboardButton("🌍 English", callback_data="lang_en"),
)

# Menu keyboards per language
menu_kb_cz = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("🧾 Menu a nabídka", callback_data="menu_cz"),
    InlineKeyboardButton("🕐 Otevírací doba", callback_data="hours_cz"),
    InlineKeyboardButton("📍 Kde nás najdete", callback_data="where_cz"),
    InlineKeyboardButton("📞 Kontakt / Rezervace", callback_data="contact_cz"),
    InlineKeyboardButton("📦 Předobjednávka", callback_data="preorder_cz"),
    InlineKeyboardButton("😎 Důvody kávu", callback_data="reasons_cz"),
)

menu_kb_en = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("🧾 Menu & Offerings", callback_data="menu_en"),
    InlineKeyboardButton("🕐 Opening Hours", callback_data="hours_en"),
    InlineKeyboardButton("📍 How to find us", callback_data="where_en"),
    InlineKeyboardButton("📞 Contact / Reservation", callback_data="contact_en"),
    InlineKeyboardButton("📦 Pre-order", callback_data="preorder_en"),
    InlineKeyboardButton("😎 Reasons to grab a coffee", callback_data="reasons_en"),
)

# Mapping callback_data → text & next keyboard
RESPONSES = {
    # Czech
    "menu_cz": (CZ_MENU, None),
    "hours_cz": (CZ_HOURS, None),
    "where_cz": (CZ_WHERE, None),
    "contact_cz": (CZ_CONTACT, None),
    "preorder_cz": (CZ_PREORDER, None),
    "reasons_cz": (CZ_REASONS, None),
    # English
    "menu_en": (EN_MENU, None),
    "hours_en": (EN_HOURS, None),
    "where_en": (EN_WHERE, None),
    "contact_en": (EN_CONTACT, None),
    "preorder_en": (EN_PREORDER, None),
    "reasons_en": (EN_REASONS, None),
}


# ====== Handlers ======

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        "☕️ Vítejte v Coffee Perk!\n"
        "Těší nás, že jste tu. 🌟\n"
        "Prosím, vyberte si jazyk. 🗣️\n\n"
        "☕️ Welcome to Coffee Perk!\n"
        "We’re happy to see you here. 🌟\n"
        "Please choose your language. 🗣️",
        reply_markup=lang_kb,
    )


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("lang_"))
async def process_language(cb: types.CallbackQuery):
    lang = cb.data.split("_")[1]
    text = "Na co se mě můžeš zeptat:" if lang == "cz" else "What you can ask me:"
    kb = menu_kb_cz if lang == "cz" else menu_kb_en

    # Update message with menu
    await cb.message.edit_text(text)
    await cb.message.edit_reply_markup(kb)
    await cb.answer()  # remove "loading" state


@dp.callback_query_handler(lambda c: c.data in RESPONSES)
async def process_menu(cb: types.CallbackQuery):
    response_text, _ = RESPONSES[cb.data]
    # Replace message text with the section content and remove buttons
    await cb.message.edit_text(response_text)
    await cb.message.edit_reply_markup(None)
    await cb.answer()


if __name__ == "__main__":
    executor.start_polling(dp)
