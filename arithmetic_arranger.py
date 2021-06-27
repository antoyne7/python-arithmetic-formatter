from problem import Problem

def check_too_many_problems(problems):
    return len(problems) > 5

def check_incorrect_operator(problem):
    if problem.split(' ')[1] not in ('+', '-'):
        return True
    return False

def check_too_many_digits(problem):
    if len(problem.split(' ')[0]) > 4 or len(problem.split(' ')[2]) > 4:
        return True
    return False

def check_not_only_digits(problem):
    for num in [problem.split(' ')[0], problem.split(' ')[2]]:
        for digit in num:
            if not digit.isdigit(): return True
    return False

def arithmetic_arranger(problems, show_result = False):
    if check_too_many_problems(problems):
        return 'Error: Too many problems.'

    if show_result: Problem.show_result = True

    lines = ['' for _ in range(4 if show_result else 3)]

    for problem in problems:
        if check_incorrect_operator(problem):
            return 'Error: Operator must be \'+\' or \'-\'.'

        if check_too_many_digits(problem):
            return 'Error: Numbers cannot be more than four digits.'

        if check_not_only_digits(problem):
            return 'Error: Numbers must only contain digits.'
        
        p = Problem.from_string(problem)
        lines = p.add_to_lines(lines)

    arranged_problems = ''
    for line in lines:
        arranged_problems += line.rstrip() + '\n'

    return arranged_problems[:-1]

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
