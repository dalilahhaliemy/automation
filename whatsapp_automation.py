from whatsapp_automation.whatsapp_config import *

# Start sending messages
# quick_send("Hi", 'Triggering new conversation by saying "Hi"')
quick_send("test rhbk peln", "Test rhb personal loan flow")
print()
print()

# Start looping through the questions
loop_send_replies(60)
sleep(wait)

# Check if the bot completed
check_bot_completed()
