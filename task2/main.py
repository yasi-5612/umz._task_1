import keyword
import time
import re
import string
import turtle


Mysterious_File_Path = "mysterious.txt"
Puzzles_File_Path = "puzzles.txt"


def decrypt_clue(text: str):
    kw_count_list = []
    for kw in keyword.kwlist:
        kw_count_list.append((kw, text.count(kw)))

    return [x for x, y in kw_count_list]


def solve_puzzles(puzzle: str):
    puzzle = puzzle.split('\n')
    results = []
    for element in puzzle:
        try:
            results.append(bool(eval(element)))
        except Exception as e:
            results.append(False)

    return results


def generate_random_number(start, end):
    return int(float(int(time.time_ns() / 100 % 10)) / 10 * (end - start) + start)


def calculate_magic_numbers(start, end):
    expected_count = 5
    magic_numbers = []
    for i in range(expected_count):
        time.sleep(0)
        magic_numbers.append(generate_random_number(start, end))

    return magic_numbers


def exam_numbers():
    magic_numbers = calculate_magic_numbers(0, 15)
    user_answers = []
    for ind in range(len(magic_numbers)):
        while True:
            num = generate_random_number(0, 15)
            magic_numbers[ind] = num
            base4, temp = list('0000'), num
            for i in range(4):
                if temp <= 0:
                    break
                base4[3 - i] = str(temp % 2)
                temp = int(temp / 2)

            print('Enter base 10 of this number: ' + ''.join(base4))
            try:
                start_time = time.time()
                user_input = int(input())
                end_time = time.time()
                if end_time - start_time > 20:
                    print('You just have 20 seconds to answer this part.\nPlease Try Again!')
                    time.sleep(3)
                    continue
                else:
                    user_answers.append(user_input)
                break
            except:
                print('Please enter Numbers not any other characters !!!')
                continue

    print('User Answer  |  Real Answer  |  result')
    results = []
    for i in range(len(user_answers)):
        res = user_answers[i] == magic_numbers[i]
        results.append(res)
        print('\t' + str(user_answers[i]) + '\t'*4 + str(magic_numbers[i]) + '\t'*3 + str(res))

    return results


def check_pass():
    puncs = list(string.punctuation)
    users_info = []
    correct_users = []
    print('Enter count of users: ')
    user_count = int(input())
    for i in range(user_count):
        print('Enter Username: ')
        user_name = input()
        print('Enter Password: ')
        password = input()
        users_info.append((user_name, password))

    print('Correct users: ')
    for info in users_info:
        user_name, password = info
        if len(password) >= 8 and len(re.findall('[A-Z]', password)) > 0 and len(re.findall('[a-z]', password)) > 0 and any(punctuation in password for punctuation in puncs):
            print(user_name)
            correct_users.append(user_name)

    return correct_users


def unlock_vault(clues):
    word = turtle.Turtle()
    word.penup()
    word.right(180)
    word.backward(150)
    word.right(180)
    word.pendown()
    word.right(90)
    word.forward(100)
    word.right(90)
    word.forward(45)
    word.backward(45)
    word.left(-65)
    word.forward(100)

    word.penup()
    word.left(155)
    word.forward(50)
    word.right(90)
    word.forward(50)
    word.pendown()
    word.left(90)
    word.forward(40)
    word.right(90)
    word.forward(50)
    word.left(45)
    word.forward(85)
    word.penup()
    word.right(135)
    word.forward(125)
    word.right(90)
    word.forward(85)
    word.pendown()
    word.forward(40)

    word.penup()
    word.right(90)
    word.forward(42)
    word.right(90)
    word.forward(210)
    word.pendown()
    word.right(135)
    word.forward(45)
    word.right(100)
    word.forward(62)
    word.right(125)
    word.forward(45)
    word.left(90)
    word.penup()
    word.forward(35)
    word.pendown()
    word.circle(2.5)
    word.penup()
    word.left(180)
    word.forward(35)
    word.left(90)
    word.pendown()
    word.forward(65)
    word.left(90)
    word.forward(50)
    word.right(90)
    word.forward(75)
    word.right(90)
    word.forward(50)
    time.sleep(3)

    secret = ''
    for clue in clues:
        first_letter = str(clue[0])[0]
        secret += first_letter

    return secret


def main():
    with open(Mysterious_File_Path, "r") as file:
        text = file.read()
        decrypt_clue_res = decrypt_clue(text)
        file.close()

    with open(Puzzles_File_Path, "r") as file:
        puzzle = file.read()
        solve_puzzles_res = solve_puzzles(puzzle)
        file.close()

    magic_numbers_res = calculate_magic_numbers(1, 10)
    exam_numbers_res = exam_numbers()
    check_pass_res = check_pass()
    secret = unlock_vault([
        decrypt_clue_res,
        solve_puzzles_res,
        magic_numbers_res,
        exam_numbers_res,
        check_pass_res
    ])

    print('SECRET IS:  ---> ' + secret + ' <---')


if __name__ == '__main__':
    main()
