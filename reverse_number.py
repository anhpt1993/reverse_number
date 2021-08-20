# reverse number

def input_data():
    while True:
        try:
            num = int(input("Enter an integer please: "))
            if num > 0:
                return num
                break
            else:
                print("Please input a positive number")
                print()
        except Exception:
            print("Enter an integer, not decimal or string")
            print()

def reverse_number(num):
    my_string = ""
    while True:
        if num == 0:
            return my_string
            break
        else:
            my_string = my_string + str(num % 10)
            num = num // 10

if __name__ == '__main__':
    num = input_data()
    print("The reverse number of {} is {}".format(num,reverse_number(num)))