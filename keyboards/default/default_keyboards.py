from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

send_phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Telefon Raqamni Yuborish", request_contact=True)
        ]
    ], resize_keyboard=True
)

send_phone_number_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Отправить номер телефона", request_contact=True)
        ]
    ], resize_keyboard=True
)

main_menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍴 Меню")
        ],
        [
            KeyboardButton(text="📋 Мои заказы"),
            KeyboardButton(text="✍️ Оставить отзыв")
        ],
        [
            KeyboardButton(text="ℹ️ О нас"),
            KeyboardButton(text="🏘 🌐 Филиалы и социальные сети")
        ],
        [
            KeyboardButton(text="⚙️ Настройки")
        ]
    ], resize_keyboard=True
)

main_menu_back_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📥 Savat"),
            KeyboardButton(text='🏘 Asosiy menyu')
        ]
    ], resize_keyboard=True
)

main_menu_back_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📥 Корзина"),
            KeyboardButton(text='🏘 Главное меню')
        ]
    ], resize_keyboard=True
)

main_menu_uzb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍴 Menyu")
        ],
        [
            KeyboardButton(text="📋 Mening Buyurtmalarim"),
            KeyboardButton(text="✍️ Izoh Qoldirish")
        ],
        [
            KeyboardButton(text="ℹ️ Biz Haqimizda"),
            KeyboardButton(text="🏘 🌐 Filiallar va Ijtimoy Tarmoqlar")
        ],
        [
            KeyboardButton(text="⚙️ Sozlamalar")
        ]
    ], resize_keyboard=True
)

settings_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Tilni O'zgartirish / 🇷🇺 Выберите язык")
        ],
        [
            KeyboardButton(text="👤 Изменить имя фамилию"),
            KeyboardButton(text="📞 Изменить номер телефона")
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ], resize_keyboard=True
)

cancel_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

cancel_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Отмена")
        ]
    ], resize_keyboard=True
)

admins_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🌐 Radius sozlamalari"),
        ],
        [
            KeyboardButton(text=f"👥 Foydalanuvchilar")
        ],
        [
            KeyboardButton(text=f"⚙️🍴 Menyuni o'zgartirish"),
            KeyboardButton(text=f'👤 Adminlar'),
        ],
        [
            KeyboardButton(text=f'✅ Xabar yuborish'),
            KeyboardButton(text=f'✅⚙️ Xabar yuborish sozlamalari')
        ],
        [
            KeyboardButton(text=f"📍 Filiallar"),
            KeyboardButton(text=f"💸 To'lov turlari")
        ],
        [
            KeyboardButton(text=f"🆔 Buyurtmalar"),
            KeyboardButton(text=f"ℹ️ Ma'lumot o'zgartirish"),
        ],
        [
            KeyboardButton(text=f"🌐 Ijtimoiy tarmoq qo'shish"),
            KeyboardButton(text=f'🍴 Menyu')
        ]
    ], resize_keyboard=True
)

payment_settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🚫 To'lov holatini o'chirish"),
            KeyboardButton(text=f"🗑 To'lov usulini olib tashlash")
        ],
        [
            KeyboardButton(text=f"➕ Yangi tolov usulini qoshish"),
            KeyboardButton(text=f"👍 Tolov holatini yoqish")
        ],
        [
            KeyboardButton(text=f"🏘 Asosiy menyu")
        ]
    ], resize_keyboard=True
)

settings_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'➕🍴 Taom qoshish'),
            KeyboardButton(text=f'🚫🍴 Menyu ochirish'),
        ],
        [
            KeyboardButton(text=f"🍴➕ Yangi menyu qoshish"),
            KeyboardButton(text=f"🔧🍴 Menyu nomini o'zgartirish")
        ],
        [
            KeyboardButton(text=f'🚫🍴 Taom olib tashlash'),
            KeyboardButton(text=f"🔧💰 Taom narxini o'zgartirish"),
        ],
        [
            KeyboardButton(text=f"🖼🍴 Menyu rasmini o'zgartirish"),
            KeyboardButton(text=f"🖼 Asosiy menyu rasmini o'zgartirish")
        ],
        [
            KeyboardButton(text=f"🔧🖼 Taom rasmini o'zgartirish"),
            KeyboardButton(text=f"🔧✍️ Taom nomini o'zgartirish"),
        ],
        [
            KeyboardButton(text=f"🏘 Asosiy menyu")
        ]
    ], resize_keyboard=True
)

admins_settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'➕👤 Yangi admin qoshish'),
            KeyboardButton(text=f'🚫👤 Admin olib tashlash')
        ],
        [
            KeyboardButton(text=f'📄👤 Adminlar'),
            KeyboardButton(text="🏘 Asosiy menyu")
        ]
    ], resize_keyboard=True
)

curers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"➕🚚 Yangi kuryer qoshish"),
            KeyboardButton(text=f"🚫🚚 Kuryer olib tashlash")
        ],
        [
            KeyboardButton(text=f"📄🚚 Kuryerlar"),
            KeyboardButton(text=f"🏘 Asosiy menyu")
        ]
    ], resize_keyboard=True
)

yes_no_def = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Xa'),
            KeyboardButton(text="❌ Yo'q")
        ]
    ], resize_keyboard=True
)

yes_no_def_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Да'),
            KeyboardButton(text='❌ Нет')
        ]
    ], resize_keyboard=True
)

locations = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🗺 Mening manzillarim")
        ],
        [
            KeyboardButton(text=f"📍 Joylashuv yuborish", request_location=True),
            KeyboardButton(text=f"❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

locations_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🗺 Мои адреса")
        ],
        [
            KeyboardButton(text=f"📍 Отправить местоположение", request_location=True),
            KeyboardButton(text=f"❌ Отмена")
        ]
    ], resize_keyboard=True
)

waiting_card_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🚚🏃 Kuryer kelgach karta korsatsin")
        ],
        [
            KeyboardButton(text=f"❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

waiting_card_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🚚🏃 Когда курьер придет, покажите карту")
        ],
        [
            KeyboardButton(text=f"❌ Отмена")
        ]
    ], resize_keyboard=True
)

settings_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"👤 Ism Familyani O'zgartirish"),
            KeyboardButton(text=f"📞 Telefon Raqamni O'zgartirish"),
        ],
        [
            KeyboardButton(text=f"🇺🇿 🔁 🇷🇺 Tilni O'zgartirish"),
            KeyboardButton(text=f"🏘 Asosiy Menyu")
        ]
    ], resize_keyboard=True
)

settings_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"👤 Изменить имя Фамилию"),
            KeyboardButton(text=f"📞 Изменить номер телефона"),
        ],
        [
            KeyboardButton(text=f"🇺🇿 🔁 🇷🇺 Изменить язык"),
            KeyboardButton(text=f"🏘 Главное меню")
        ]
    ], resize_keyboard=True
)
go_or_ordering = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🏃 Borib olish"),
            KeyboardButton(text=f"🚖 Yetkazib berish")
        ],
        [
            KeyboardButton(text=f"❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

go_or_ordering_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🏃 Самовывоз"),
            KeyboardButton(text=f"🚖 Доставка")
        ],
        [
            KeyboardButton(text=f"❌ Отмена")
        ]
    ], resize_keyboard=True
)

filials_bttn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"➕📍 Filial qo'shish"),
            KeyboardButton(text=f"📍 Barcha filiallar")
        ],
        [
            KeyboardButton(text=f"👐 Filial ochib qoyish"),
            KeyboardButton(text=f"🚫📍 Filial yopish")
        ],
        [
            KeyboardButton(text=f'👤 Filial admin qoshish'),
            KeyboardButton(text=f'👤🚫 Filial admin olib tashlash'),
        ],
        [
            KeyboardButton(text="🗑📍 Filial olib tashlash"),
            KeyboardButton(text=f"❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

send_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"📍 Joylashuv yuborish", request_location=True)
        ],
        [
            KeyboardButton(text=f"❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

filials_and_socials_bttn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"📍 Filiallar"),
            KeyboardButton(text=f"🌐 Ijtimoiy tarmoqlar")
        ],
        [
            KeyboardButton(text=f"❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

radius_settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"💸🌐 Radius narxlari"),
            KeyboardButton(text=f"❌🌐 Radius ochirish")
        ],
        [
            KeyboardButton(text=f"➕🌐 Radius qoshish"),
            KeyboardButton(text=f"🌐 Radius o'zgartirish")
        ],
        [
            KeyboardButton(text=f"❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

filials_and_socials_bttn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"📍 Филиалы"),
            KeyboardButton(text=f"🌐 Социальные сети")
        ],
        [
            KeyboardButton(text=f"❌ Отмена")
        ]
    ], resize_keyboard=True
)
