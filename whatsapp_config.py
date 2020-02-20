from selenium import webdriver               # to use selenium to open website
from time import sleep
import sys
from whatsapp_automation.questions_card import Logger
from datetime import datetime


# log the output to a file
sys.stdout = Logger(r"C:/Users/Diyanah/Documents/Selenium Log/wa_1802_05.txt")

# print current time
date = datetime.now().date().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%I:%M:%S %p")
print(date, time)


# defining CC/Loan flow
flow = input("Enter 'CC' or 'Loan' to select the flow : ")

if flow == "CC":
    from whatsapp_automation.questions_card import questions
elif flow == "Loan":
    from whatsapp_automation.questions_peln import questions
else:
    print("ERROR - Start again")

print(str(flow))


# Using selenium chrome webdriver to launch the whatsapp web
driver = webdriver.Chrome(executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")    #need to specify where the chromedriver located  # to open chrome
driver.get("https://web.whatsapp.com/")   # to open the website

# Define the chat user name that we want to automate
name = "Jirnexu Dev - Banking"    # Jirnexu Dev - Banking / Jirnexu Dev Insurance / RinggitPlus
global wait
wait = 17
driver.implicitly_wait(wait)
print("Scan the QR code")
sleep(wait)
input("Press anything after scanning the QR code")   # after scanning the QR code
print()
branch_name = input("Input branch name to be tested on: ")
print(branch_name)


# Search the user name element and clicking it
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()


# Search the message input box
msg_box = driver.find_element_by_class_name('_3u328')


# Sending the message with variable 'msg'
def send_message(mesg):
    msg_box.send_keys(mesg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()


# Automate sending message with note
def quick_send(replies, note):
    send_message(replies)
    print(note)
    sleep(wait)


# Check the latest msg sent
def check_last_msg_sent():
    msg_got = driver.find_elements_by_css_selector("span._F7Vk.selectable-text.invisible-space.copyable-text")      # replace space with . and find the text
    global msg                                      # define this to make it accessible outside the function. This replace the definition of msg
    msg = [message.text for message in msg_got]     # read the text and store in a list


# check for download button for terms of use exist
def check_docs_downloadable(index, pass_note, fail_note):
    try:
        global download_icon
        download_icon = driver.find_elements_by_class_name("_1qlav")
        download_icon[index].click()
        print(pass_note)
    except:
        print(fail_note)


# Get text list
def get_text_list(title, replies, note, *index):
    option_list = driver.find_elements_by_css_selector("strong._F7Vk.selectable-text.invisible-space.copyable-text")
    global option
    option = [opt.text for opt in option_list]

    print(title)
    for i in index:
        print("  " + str(option[i]))

#    replies = input("Selection : ")               # not needed if normal automation
    quick_send(replies, note)
    sleep(wait)
    print()
    print()


# looping the dictionaries to find answer to the latest question
def loop_send_replies(a):          # how many times want to run through latest question in dictionary and send replies
    try:
        for i in range(a):
            check_last_msg_sent()
            global keys
            global val

            if str.__contains__(msg[-1], "our terms of use"):
                check_docs_downloadable(-1, "Success downloading RinggitPlus Terms of Use", "ERROR - Unable to download RinggitPlus Terms of Use")
                print()
                print()

            elif str.__contains__(msg[-1], "terms and conditions"):
                check_docs_downloadable(-2, "Success downloading Bank T&C", "ERROR - Unable to download Bank T&C")
                sleep(wait)
                check_docs_downloadable(-1, "Success downloading Bank PDS", "ERROR - Unable to download Bank PDS")
                sleep(wait)
                print()
                print()

            elif str.__contains__(msg[-1], "just say 'skip'"):
                attach_icon = driver.find_element_by_xpath('//div[@title = "Attach"]')
                attach_icon.click()
                image_icon = driver.find_element_by_xpath(
                    '//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_icon.send_keys(r'C:/Users/Diyanah/Pictures/front.png')
                sleep(wait)
                send_icon = driver.find_element_by_xpath('//span[@data-icon = "send-light"]')
                send_icon.click()
                print("Success sending front IC")
                sleep(20)

            elif str.__contains__(msg[-1], "Please send me the back of your IC"):
                attach_icon = driver.find_element_by_xpath('//div[@title = "Attach"]')
                attach_icon.click()
                image_icon = driver.find_element_by_xpath(
                    '//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_icon.send_keys(r'C:/Users/Diyanah/Pictures/back.png')
                sleep(wait)
                send_icon = driver.find_element_by_xpath('//span[@data-icon = "send-light"]')
                send_icon.click()
                print("Success sending back IC")
                sleep(20)
                print()
                print()

            elif str.__contains__(msg[-1], "Not what you're looking for"):  # card or product selection
                get_text_list("Top 3 products are: ", "2", "User choose the first product", -12, -9, -6)

            elif str.__contains__(msg[-5], "branch"):
                get_text_list("Branches are: ", "1", "User select the first branch", -8, -6, -4, -2)

            for k, v in questions.items():
                if str.__contains__(msg[-1], k):                     # if the question is from dictionaries
                    keys = k
                    val = v
                    print(msg[-1])
                    quick_send(val[0], val[1])
                    print()
                    print()

            keys = ""
            val = ""
    except:
        pass


# Check if the bot completed
def check_bot_completed():
    check_last_msg_sent()
    if str.__contains__(msg[-1], "Thank you"):
        print(msg[-2])
        print(msg[-1])
    elif str.__contains__(msg[-2], "Thank you"):
        print(msg[-2])
        print(msg[-1])
    elif str.__contains__(msg[-3], "Thank you"):
        print(msg[-3])
        print(msg[-2])
        print(msg[-1])
    else:
        print("ERROR - Bot not complete")


# Start sending messages
quick_send("/branch "+str(branch_name), "")
quick_send("/new", "Starting new chat")
quick_send("/transcriptid", "")
check_last_msg_sent()
print("Transcript ID :", msg[-1])
