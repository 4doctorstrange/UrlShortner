import random
import string

class shortner:
    token_size = 5

    def __init__(self, token_size=None):
        self.token_size = token_size if token_size is not None else 5

    '''
    In below function we have a string of ascii letters -'letters' and we are 
    returing a string of 5 chars randomly chosen from 'letters'
    '''
    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token_size))    
