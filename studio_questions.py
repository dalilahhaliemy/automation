import sys


class Logger:
    def __init__(self, file):
        self.terminal = sys.stdout
        self.log = open(file, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass


questions = {
    "How can I help you today?": ["Apply for Credit Card", "Selecting Credit Cards flow"],
    "Type 3 to Contact RinggitPlus": ["Apply for Credit Card", "Selecting Credit Cards flow"],
    "already have a credit card": ["No, it's my first card", "This is user's first card"],
    "kind of credit card": ["No preference", "Selecting user has no preferences"],
    "Islamic credit card": ["No, not really", "User does not mind islamic/conventional credit card"],
    "salary": ["RM5000", "Salary input is RM5,000"],
    "your name": ["Mei Mei", "Name input is Mei Mei"],
    "Let me know your mobile number, please?": ["013-2339978", "User's phone number is '013-2339978'"],
    "email address": ["diyanah.haliemy@jirnexu.com", "Email input is 'diyanah.haliemy@jirnexu.com'"],
    "born in Malaysia": ["Yes, I'm Malaysian", "User is Malaysian"],
    "your NRIC": ["920920-05-5066", "IC number input is 920920-05-5066"],
    "Please let me know your IC number": ["920920-05-5066", "IC number input is 920920-05-5066"],
    "What's your IC number": ["920920-05-5066", "IC number input is 920920-05-5066"],
    "Is that correct?": ["Yes, this is my NRIC", "Reconfirm IC number is correct"],
#    "What's your full name": ["Chan Mei Mei", "Full name input is Chan Mei Mei", 11],
    "full name, as written on your MyKad": ["Chan Mei Mei", "Full name input is Chan Mei Mei"],
    "race": ["Malay", "User is Malay"],
    "marital status": ["Single", "User is Single"],
    "support financially": ["1", "User support 1 financially"],
    "academic qualification": ["Degree", "User's highest qualification is Degree"],
    "current residence status": ["Renting", "User renting"],
    "move in": ["January 2019", "User moved in on January 2019"],
    "employment sector": ["Private", "User employment sector is private"],
    "employment type": ["Salaried", "User employment type is salaried"],
    "join your current company": ["January 2019", "User joined current company on January 2019"],
    "terms of use": ["I have read and I agree", "User has read the Term of use"],
    "credit score": ["No, I don't need to know if I'm applying for the best card", "User do not let R+ run credit score"],
    # choose product
    "company do you": ["RinggitPlus", "User's company name is RinggitPlus"],
    "company you work": ["RinggitPlus", "User's company name is RinggitPlus"],
    "office address": ["Confirm", "Confirming company address populated by chatbot"],
    "03-7890 0808": ["Yes, correct", "Confirming office number populated by chatbot"],
    "nature of business of your": ["Banking & Finance", "Selecting Banking & Finance as nature of business"],
    # this is RHB flow
    "type out your company's": ["Charity services", "User typed Charity Services as nature of business"],
    "Health Services": ["Health Services", "User select the first option"],
    "What's your occupation": ["Others", "Selecting Others as occupation"],
    "type out your occupation": ["App tester", "User typed app tester as occupation"],
    "Applications": ["1", "User select the first option"],
    # below is normal flow
    "name of your husband": ["Ahmad Ibrahim", "Husband name is Ahmad Ibrahim"],
    "husband's mobile phone number": ["013-54667899", "Husband phone number is 013-54667899"],
    "husband currently employed": ["1", "Husband currently employed"],
    "company your husband": ["Telekom Malaysia", "Husband's company is Telekom Malaysia"],
    "pre-existing debts": ["No", "User do not have any debt"],
    "department": ["IT", "User works in IT department", 30],
    "job title": ["App tester", "User's job title is App tester"],
    "your profession": ["Executive", "User is an executive"],
    "Executive": ["Executive", "User is an executive"],
    "first employer": ["1", "RinggitPlus is user's first employer"],
    "after tax": ["4500", "User's income after tax is RM4,500", 31],
    "financial commitment": ["No, continue", "User has no other financial commitment", 32],
    "What kind of property do you live in?": ["Condo", "User lives in a condo", 33],
    "What is the type of property you're living in?": ["Condo", "User lives in a condo"],
    "residence name": ["Seri Maya", "User's residence name is Seri Maya", 34],
#    "home address": ["1", "User confirm the home address"],
    "unit number": ["G-12-13", "User's unit number is 'G12-13'", 35],
    "landline number": ["03-3456 9089", "User's home phone number is 03-3456 9089", 36],
    "many children": ["0", "User do not have any children"],
    "security purpose": ["Chan Lin Lin", "User's mother name is Chan Lin Lin", 37],
    "person not living": ["Chan Lin Lin", "User's emergency contact is Chan Lin Lin", 38],
    "mobile phone number": ["019-3456 8990", "Emergency contact number is 019-3456 8990", 39],
    "related to you": ["Parent", "Relation is Parent", 40],
    "address your emergency contact": ["Mdm", "Mdm Chan Lin Lin", 41],
    "full name to be printed": ["Yes, use full name", "User use full name on the card"],
    "mailing address": ["Send to office", "Office is correspondence address", 42],
    "correspondence address": ["Send to office", "Office is correspondence address", 42],
    "collect your card": ["Near work", "Collect card near work"],
    # branches
    "relative working": ["No", "User do not have any relative working at the bank"],
    # TnC PDS
    "terms and conditions": ["I have read and I agree", "User has read and agree to the T&Cs"],
    "review your details": ["All looks correct", "User do not want to perform any changes to the data"],
    "Do you want me to check for you?‌": ["No, don't check", "User do not want to check her credit score"]
}

'''
    "Home Loans": ["1", "Selecting personal loan flow by typing 1"],
    "How much would you like to borrow": ["RM100,000", "User borrow RM100,000"],
    "How much do you want to borrow": ["RM100,000", "User borrow RM100,000"],
    "purpose of this loan": ["2", "Loan purpose is Education"],
    "Islamic loan": ["1", "User does not mind islamic/conventional loan by typing 1"],
    "existing loans": ["RM0.00", "User do not have any existing loans"],
    # product are listed
    "eligible to apply for up to": ["1", "User proceed with current loan amount"],
    "repayment period": ["1", "User select 1st selection as payment period"],
    "loan details": ["1", "User proceed with loan details"],
    "get your loan": ["2", "Loan disbursed near work", 42],
'''
# print(len(questions))