from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from mailstatus import GameSession, get_current_player, get_specific_session


def game_status(update: Update, context: CallbackContext) -> None:
    game = get_specific_session()
    current_player = get_current_player(game)
    message = f"""Freeciv Play-By-Email game status
    Players: {", ".join(game.players)}
    Turn: {game.turn}
    On move: {current_player}
    Last played: {game.last_played}
    Time left: {game.hours_left} hours"""
    update.message.reply_text(message)

def greet(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""FreeCiv Play-By-Email status bot

    /who - shows you the current player on the move
    /status - gives you stats about the current game
    """)

def player_turn(update: Update, context: CallbackContext) -> None:
    game = get_specific_session()
    update.message.reply_text(f"{get_current_player(game)} should make the move now")


updater = Updater("BotFather output goes here")

updater.dispatcher.add_handler(CommandHandler("status", game_status))
updater.dispatcher.add_handler(CommandHandler("who", player_turn))
updater.dispatcher.add_handler(CommandHandler("start", greet))

updater.start_polling()
updater.idle()
