
users_data = {}
vip_developer = 293125876
channel_id = 1383113458
group_id = -1001135607371
#Importing Modules
try:
    import os, telegram, time, sys, logging
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
    from telegram.ext.dispatcher import run_async
    from functools import wraps
    from pprint import pprint
except ImportError as e:
    print("Problem: ",e)
    exit()

#Bot Data (Please insert bot token here!)
namebot = 'test-bot24'
verbot  = 'v1' #<== You can change this version with your real bot version
tokenbot= '565213646:AAEvaSxCWSIE5wO45SvmnRvupDH0ERTMN1Q' #<-- Put your bot token here!


#polling setup
try:
    updater= Updater(tokenbot)
except ValueError as e:
    print("Please insert your tokenbot!")
    exit()

#webhook setup
#
#Webhook(Heroku):
#-------------------------------
PORT = int(os.environ.get('PORT', '5000'))
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=tokenbot)

updater.bot.set_webhook("https://test-bot24.herokuapp.com/" + tokenbot)
#--------------------------------

#handling command
dispatcher = updater.dispatcher

#logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#####################################################################################################################
#COMMAND
#####################################################################################################################

@run_async
def start(bot, update):
    msg= "Hello! ^_^ I am GOOP Test Bot"
    bot.send_message(chat_id=update.message.chat_id, text=msg)

@run_async
def fuck(bot, update):
    msg= "Fuck you asshole!!"
    bot.send_message(chat_id=update.message.chat_id, text=msg)
    
@run_async
def developer(bot, update):
    msg= "Contact my developer:- @dharmaraj_24"
    bot.send_message(chat_id=update.message.chat_id, text=msg)
    
@run_async
def help(bot, update):
    msg= "*Here is a list of Available Commands!* \n"
    msg+= "/developer - Meet my Developer \n"
    msg+= "/myid - Shows your Telegram ID \n"
    msg+= "/suggestion - Let us know how can we improvement \n"
    bot.send_message(chat_id=update.message.chat_id, text=msg)
    
@run_async
def myid(bot, update):
	


	chatid  = "`"+str(update.message.chat_id)+"`"
	msg 	= "*Your chat id*: "+chatid

	bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)

@run_async
def pingteam(bot, update):
    if update.message.chat_id == -1001386729992:
        bot.send_message(chat_id=update.message.chat_id, text="Need Assistance @dharmaraj_24 @Asaf31214 @VrozAnims2003")
			

@run_async	
def post(bot, update):
    if update.message.chat_id == 293125876:
        bot.send_message(chat_id='@ClashersShield', text="This is a test message")
		

	

		
	
	
#####################################################################################################################

#configure command
start_handler      = CommandHandler('start', start)
fuck_handler       = CommandHandler('fuck', fuck)
developer_handler  = CommandHandler('developer', developer)
help_handler       = CommandHandler('help', help)
myid_handler       = CommandHandler('myid', myid)
pingteam_handler   = CommandHandler('pingteam', pingteam)
post_handler       = CommandHandler('post', post)
#####################################################################################################################

#set command

dispatcher.add_handler(start_handler)
dispatcher.add_handler(fuck_handler)
dispatcher.add_handler(developer_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(myid_handler)
dispatcher.add_handler(pingteam_handler)
dispatcher.add_handler(post_handler)

#####################################################################################################################

#start polling
print(namebot,' ',verbot,' : Start!')
updater.start_polling()

#updater.idle() #untuk menjalankan heroku webhook

#####################################################################################################################
#FOR MORE INFORMATION, CHECK htps://github.com/python-telegram-bot/python-telegram-bot
