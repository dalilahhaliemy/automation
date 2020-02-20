class Chatbot_text:
    def __init__(self, text, replies, note, q_number):
        self.text = text
        self.replies = replies
        self.note = note
        self.q_number = q_number

    def __str__(self):
        return "{}\n{}\n{}\n{}".format(self.text, self.replies, self.note, self.q_number)
