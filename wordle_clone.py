import pyinputplus as pyip
def get_user_guess():
    guess = pyip.inputStr(
    prompt='Enter a five-letter word: ',
    allowRegexes=[r'^[A-Za-z]{5}$'],
    blockRegexes=[r'.*'])  # Block everything not explicitly allowed
    return guess.lower()
answer='snake'
guess=get_user_guess()
if guess==answer:
    print("Correct")
else:
    print('Wrong')

