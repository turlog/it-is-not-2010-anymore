def ask_old(question, *choices):
    while True:
        answer = input(f"\n{question} ")
        if answer in choices:
            return answer
        print(f"Please answer one of {', '.join(choices)}")


def ask_new(question, *choices):
    while (answer := input(f"\n{question} ")) not in choices:
        print(f"Please answer one of {', '.join(choices)}")
    return answer
