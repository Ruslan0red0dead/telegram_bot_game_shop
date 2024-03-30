from aiogram import Bot, types, Dispatcher, executor
import aiogram.utils.markdown as fmt
from game_api import Api_data
from keyboards import button
from globals import Globals
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# introduction
@dp.message_handler(commands = 'start')
async def start_bot(message: types.Message):
	await message.answer('Enter the name of the game')

# this function will display a scrolling menu of games
@dp.message_handler()
async def bot_send_message(message: types.Message):

	# is a replacement for the global function
	# to add data to the process_callback_button1 function
	Globals.g_a = Api_data(message.text)

	# we need the 'index' variable to know how many games are in the list
	index = len(Globals.g_a)

	try:
		await message.answer(
			fmt.text(
				fmt.hide_link(Globals.g_a[1][1]),
				),
			parse_mode="HTML",
			reply_markup=button(Globals.g_a[1][1], f"1/{index}")
			)

	except IndexError:
		await message.answer('Game not found')


# button
@dp.callback_query_handler(lambda c: c.data == 'back' or 'NEXT')
async def process_callback_button1(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)

	index = len(Globals.g_a)
	
	async def bot_keyboards():
		# 'callback_query.message.edit_text' is needed to change the displayed game in the list to the next game in the list 
		await callback_query.message.edit_text(
			fmt.text(
				fmt.hide_link(Globals.g_a[0][1]),
				),
			parse_mode="HTML",
			reply_markup=button(Globals.g_a[0][1], f"{Globals.g_a[0][0]}/{index}")
			)

	if callback_query.data == 'NEXT':
		# this code adds a game from the beginning of the list to the end and adds a game from the end of the list to the beginning
		Globals.g_a.append(Globals.g_a[0])
		Globals.g_a.remove(Globals.g_a[0])
		await bot_keyboards()

	if callback_query.data == 'back':
		# this code works the other way around
		Globals.g_a.insert(0, Globals.g_a[-1])
		Globals.g_a.pop(index)
		await bot_keyboards()

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)