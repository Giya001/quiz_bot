from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    fullname=State()
    phone=State()

