# utils


def check_answer(proper_answer, given_answer):
    errors = 0
    length = max(len(proper_answer), len(given_answer))
    for i in range(length):
        try:
            if not given_answer[i] == proper_answer[i]:
                errors += 1
        except IndexError:
            errors += 1

    if errors == 0:
        result = 'Perfect'
    elif errors == 1:
        result = 'Good'
    else:
        result = 'Bad'

    return result
