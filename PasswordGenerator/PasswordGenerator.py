import random


class generate_password:

    def __init__(self):
        self.upper_case_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lower_case_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.special_character = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=',
                                  '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def generator_4(self):
        str = ""
        while 1:
            upper_ind = random.randint(0, 25)
            lower_ind = random.randint(0, 25)
            special_ind = random.randint(0, 28)
            number_ind = random.randint(0, 9)
            str = str + self.upper_case_letter[upper_ind] + self.lower_case_letter[lower_ind] + self.numbers[
                number_ind] + self.special_character[special_ind]
            if len(str) == 4:
                break
            else:
                continue

        print(str)

    def generator_8(self):
        str = ""
        while 1:
            upper_ind = random.randint(0, 25)
            lower_ind = random.randint(0, 25)
            special_ind = random.randint(0, 28)
            number_ind = random.randint(0, 9)
            str = str + self.upper_case_letter[upper_ind] + self.lower_case_letter[lower_ind] + self.numbers[
                number_ind] + self.special_character[special_ind]
            if len(str) == length:
                break
            else:
                continue
        print(str)


if __name__ == "__main__":
    p = generate_password()
    while 1:
        length = int(input(print("Enter the password length 4,8 or 0 to quit the system")))
        if length == 0:
            print("Thank you for using this code!")
            break
        elif length == 4:
            p.generator_4()
        elif length == 8:
            p.generator_8()
        else:
            print("Invalid entry, try again: ")
