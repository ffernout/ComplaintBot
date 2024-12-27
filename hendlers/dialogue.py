from aiogram import Router,  types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


review_button = Router()

class Questions(StatesGroup):
    name = State()
    contact = State()
    extra_comments = State()


@review_button.message(Command("questions"))
async def ask_name(message: types.Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(Questions.contact)


@review_button.message(Questions.contact)
async def ask_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Как с вами можно связаться? Номер или Instagram")
    await state.set_state(Questions.extra_comments)

    await state.update_data(contact=message.text)
    await message.answer("Есть дополнительные жалобы?")
    await state.set_state(Questions.extra_comments)

