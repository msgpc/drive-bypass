from telegram.ext import CommandHandler
from telegram import InlineKeyboardMarkup
from bot import AUTHORIZED_CHATS, dispatcher
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage, sendMarkup
from bot.helper.telegram_helper import button_builder, bot_commands
from bot.helper.parser import get_gp_link


def gplink(update, context):
    buttons = button_builder.ButtonMaker()
    buttons.buildbutton("š£šæš¶šŗš² šš¼šš", "https://t.me/prime_Botz")
    buttons.buildbutton("šš¼š¶š»", "https://t.me/PrimexCloud")
    reply_markup = InlineKeyboardMarkup(buttons.build_menu(1))
    try:
       query = update.message.text.split()[1]
    except:
       sendMarkup('<b>š¦š²š»š± šš½š¹š¶š»šø šš¶š»šøš š®š¹š¼š»š“ šš¶ššµ š°š¼šŗšŗš®š»š±</b>', context.bot, update, reply_markup)
       return

    m = sendMessage('ššš½š®ššš¶š»š“ šš¼ššæ šš½š¹š¶š»šø šš¶š»šø \nšš”šššØš š¬ššš© š š¢šš£šŖš©š.', context.bot, update)
    link = get_gp_link(query)
    deleteMessage(context.bot, m)
    if not link:      
       sendMessage("š¦š¼šŗš²ššµš¶š»š“ šš²š»š ššæš¼š»š“\nš§šæš š®š“š®š¶š» š¹š®šš²šæ..š„ŗ  ", context.bot, update)
    else:
       sendMessage(f'š¬š¼ššæ šš¶š»šø ššš½š®ššš²š± ā \n\nššš½š®ššš²š± šš¶š»šø: <code>{link}</code>', context.bot, update)

gplink_handler = CommandHandler("gplink", gplink,
                               filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(gplink_handler)

