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
    "Type 3 to Contact RinggitPlus": ["1", "Selecting Credit Cards by typing 1", 1],
    "already have a credit card": ["1", "Selecting user's first card by typing 1", 2],
    "kind of credit card": ["2", "Selecting user has no preferences by typing 1", 3],
    "Islamic credit card": ["1", "User does not mind islamic/conventional credit card by typing 1"],
    "salary": ["RM5000", "Salary input is RM5,000"],
    "your name": ["Mei Mei", "Name input is Mei Mei"],
    "email address": ["diyanah.haliemy@jirnexu.com", "Email input is 'diyanah.haliemy@jirnexu.com'", 7],
    "born in Malaysia": ["1", "Selecting 1, user is Malaysian", 8],
    "your NRIC": ["920920-05-5066", "IC number input is 920920-05-5066", 9],
    "your IC number": ["920920-05-5066", "IC number input is 920920-05-5066", 9],
    "Is that correct?": ["1", "Selecting 1, IC number is correct", 10],
#    "What's your full name": ["Chan Mei Mei", "Full name input is Chan Mei Mei", 11],
    "full name, as written on your MyKad": ["Chan Mei Mei", "Full name input is Chan Mei Mei", 11],
    "race": ["1", "Selecting 1, user is Malay", 12],
    "marital status": ["1", "Selecting 1, user is Single", 13],
    "support financially": ["1", "User support 1 financially", 14],
    "academic qualification": ["2", "User's highest qualification is Degree", 15],
    "current residence status": ["1", "User renting", 16],
    "move in": ["January 2019", "User moved in on January 2019", 17],
    "employment sector": ["1", "User employment sector is private", 18],
    "employment type": ["1", "User employment type is salaried", 18],
    "join your current company": ["January 2019", "User joined current company on January 2019", 19],
    # check for downloadable R+ TnC here
    "terms of use": ["1", "User has read the Term of use", 20],
    "credit score": ["1", "User let R+ run credit score", 21],
    # send IC front and back
    "company do you": ["RinggitPlus", "User's company name is RinggitPlus", 26],
    "company you work": ["RinggitPlus", "User's company name is RinggitPlus", 26],
    "office address": ["1", "Confirming company address populated by chatbot", 27],
    "03-7890 0808": ["1", "Confirming office number populated by chatbot", 28],
    # this is RHB flow
    "nature of business of your": ["7", "Selecting Others as nature of business", 29],
    "type out your company's": ["Charity services", "User typed Charity Services as nature of business"],
    "Health Services": ["1", "User select the first option"],
    "What's your occupation": ["7", "Selecting Others as occupation", 29],
    "type out your occupation": ["App tester", "User typed app tester as occupation"],
    "Applications": ["1", "User select the first option"],
    # below is normal flow
    "name of your husband": ["Ahmad Ibrahim", "Husband name is Ahmad Ibrahim"],
    "husband's mobile phone number": ["013-54667899", "Husband phone number is 013-54667899"],
    "husband currently employed": ["1", "Husband currently employed"],
    "company your husband": ["Telekom Malaysia", "Husband's company is Telekom Malaysia"],
    "pre-existing debts": ["1", "User do not have any debt"],
    "department": ["IT", "User works in IT department", 30],
    "job title": ["App tester", "User's job title is App tester"],
    "your profession": ["2", "User is an executive"],
    "first employer": ["1", "RinggitPlus is user's first employer"],
    "after tax": ["4500", "User's income after tax is RM4,500", 31],
    "financial commitment": ["1", "User has no other financial commitment", 32],
    "Condo": ["2", "User lives in a condo", 33],
    "residence name": ["Seri Maya", "User's residence name is Seri Maya", 34],
    "home address": ["1", "User confirm the home address"],
    "unit number": ["G-12-13", "User's unit number is 'G12-13'", 35],
    "landline number": ["03-3456 9089", "User's home phone number is 03-3456 9089", 36],
    "many children": ["0", "User do not have any children"],
    "security purpose": ["Chan Lin Lin", "User's mother name is Chan Lin Lin", 37],
    "person not living": ["Chan Lin Lin", "User's emergency contact is Chan Lin Lin", 38],
    "mobile phone number": ["019-3456 8990", "Emergency contact number is 019-3456 8990", 39],
    "related to you": ["2", "Relation is Parent", 40],
    "address your emergency contact": ["3", "Mdm Chan Lin Lin", 41],
    "full name to be printed": ["1", "User use full name on the card"],
    "mailing address": ["1", "Office is correspondence address", 42],
    "correspondence address": ["1", "Office is correspondence address", 42],
    "collect your card": ["2", "Collect card near work"],
    # branches
    "relative working": ["1", "User do not have any relative working at the bank"],
    # TnC PDS
    "terms and conditions": ["1", "User has read and agree to the T&Cs"],
    "review your details": ["All looks correct", "User do not want to perform any changes to the data", 44]
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