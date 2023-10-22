class Reader():
    def __init__(self, text):
        self.text = text
        self.len = len(text)
        self.current_letter = -1
    
    def has_more_char(self, n = 1):
        return self.len > self.current_letter + n

    def next_char(self):
        if self.has_more_char():
            self.current_letter += 1
            return self.text[self.current_letter]
        else:
            return None

    def peek_next(self):
        if self.has_more_char():
            return self.text[self.current_letter + 1]