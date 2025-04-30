from aiogram.dispatcher.filters.state import State,StatesGroup


class KinoState(StatesGroup):
    kino=State()
    kod=State()


class ReklamaState(StatesGroup):
    reklam=State()
    confirm=State()
