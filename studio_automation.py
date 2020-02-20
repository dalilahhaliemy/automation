from selenium import webdriver    #to use selenium to open website
from selenium.webdriver.common.keys import Keys
from time import sleep
from studio_automation.studio_questions import questions
import sys
from studio_automation.studio_questions import Logger
from datetime import datetime


# log the output to a file
sys.stdout = Logger(r"C:/Users/Diyanah/Documents/Selenium Log/studio_1802_04.txt")

# print current time
date = datetime.now().date().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%I:%M:%S %p")
print(date, time)

# Using selenium chrome webdriver to launch the chrome incognito
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_option, executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")    #need to specify where the chromedriver located  to open chrome
driver.get("https://banking.test.ringgitplus.com/")   # to open the website

# clicking 'Continue with Google'
driver.implicitly_wait(10)
wait = 15

# click google sign
sign_in = driver.find_elements_by_css_selector("button.btn.google-button.socialButton-customizable")
sign_in[-1].click()

# input email
email_placeholder = driver.find_element_by_id("identifierId")
email = "diyanah.haliemy@jirnexu.com"
email_placeholder.send_keys(email)
driver.find_element_by_id("identifierNext").click()

# input password
pwd_placeholder = driver.find_element_by_name("password")
pwd = "password123~!"
pwd_placeholder.send_keys(pwd)
driver.find_element_by_id("passwordNext").click()

# input code receive by sms
code_placeholder = driver.find_element_by_id("idvPin")
code = str(input("Enter the G-code received: "))
print(code)
code_placeholder.send_keys(code)
driver.find_element_by_id("idvPreregisteredPhoneNext").click()

# select branch
branch_name = input("Input branch name to be tested on: ")
print(branch_name)
branch = driver.find_element_by_name(branch_name)
branch.click()
sleep(wait)

# Start the conversation
msg_box = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/input')


def send_message(replies, note):
    msg_box.send_keys(replies)
    msg_box.send_keys(Keys.ENTER)

    print(note)
    sleep(wait)


# Check the latest msg sent
def check_last_msg_sent():
    msg_got = driver.find_elements_by_css_selector("div.message-text")
    global msg                                      # define this to make it accessible outside the function. This replace the definition of msg
    msg = [message.text for message in msg_got]     # read the text and store in a list


# Send verification code for mobile number
def get_v_code():
    sleep(wait)
    xray = driver.find_elements_by_xpath("//*[@id='root']/div/ol/li[27]/ul/li[5]")
    global xray_text
    xray_text = [message.text for message in xray]     # read the text and store in a list

    print(xray_text[-1])     # print last message
    v_code = input("Enter the verification code: ")
    print(v_code)
    send_message(v_code, "Verifying mobile number")
    print()


# Get text list
def get_text_list(title, *index):
    option_list = driver.find_elements_by_css_selector("h4")
    global option
    option = [opt.text for opt in option_list]

    print(title)
    for i in index:
        print("  " + str(option[i]))


# Click button (-8 is the last index)
def click_button(index, note):
    button_list = driver.find_elements_by_css_selector("button")
    button_list[index].send_keys("\n")
    print(note)
    print()
    sleep(wait)


# looping the dictionaries to find answer to the latest question
def loop_send_replies(a):                # how many times want to run through latest question in dictionary and send replies
    try:
        for i in range(a):
            check_last_msg_sent()
            global keys
            global val

            if str.__contains__(msg[-1], "Please enter your verification code"):   # verifying phone num
                get_v_code()

            elif str.__contains__(msg[-1], "I've found"):
                get_text_list("Top 3 cards are: ", -4, -3, -2)                      # Printing top 3 cards
                click_button(-11, "Selecting 1st card")

            elif str.__contains__(msg[-1], "Please confirm this is the location of your home"):   # Confirm house address
                print(msg[-1])
                click_button(-9, "Confirming house address")

            elif str.__contains__(msg[-1], "Please select your preferred branch"):   # Selecting bank branch
                get_text_list("Branches are: ", -4, -3, -2, -1)
                click_button(-11, "Selecting 1st branch")

            ## CHECK if terms and product discosure able to open

            for k, v in questions.items():
                if str.__contains__(msg[-1], k):                     # if the question is from dictionaries
                    keys = k
                    val = v
                    print(msg[-1])
                    send_message(val[0], val[1])
                    print()

                elif str.__contains__(msg[-2], k):                     # if the question is from dictionaries
                    keys = k
                    val = v
                    print(msg[-2])
                    send_message(val[0], val[1])
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
    elif str.__contains__(msg[-1], "have a nice day"):
        print(msg[-1])
    else:
        print("ERROR - Bot not complete")


# Printing Transcript ID
trans_id = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[3]/div[5]/span[6]").get_attribute("title")
print("Transcript ID: " + trans_id)
print()

# Start looping through the questions
loop_send_replies(60)
sleep(wait)

# Check if the bot completed
check_bot_completed()
