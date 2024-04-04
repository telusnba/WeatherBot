from aiogram.utils.keyboard import ReplyKeyboardBuilder


def location_keyboard():
    main_kb = ReplyKeyboardBuilder()

    main_kb.button(text='Надіслати координати', request_location=True)
    main_kb.adjust(2)
    return main_kb.as_markup()
