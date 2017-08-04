from sys import stdin


def ask_question(question):

    print question
    answer = stdin.readline()
    return answer


def ask_yes_no_question(question):
    """
    Takes a string as a question to print
    Returns True or False as an answer
    """
    valid_response = False
    while not valid_response:
        answer = ask_question(question)
        if answer == "y\n":
            valid_response = True
        if answer == "n\n":
            valid_response = True
    return answer == "y\n"
