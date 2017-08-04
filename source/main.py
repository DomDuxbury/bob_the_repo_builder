import utils


def main():
    age = utils.ask_question("How old are you")
    print age
    yes = utils.ask_yes_no_question("Yes? (y/n)")
    print yes


if __name__ == "__main__":
    main()
