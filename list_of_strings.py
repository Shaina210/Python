
from Print_statement import repeat_hello, hello_name

def print_even_up_to_number(input_num):
    list_of_numbers= list(range(1, input_num+1))
    print(list_of_numbers)
    for number in list_of_numbers:
        if number % 2 == 0:
            print(num)

if __name__ == "__main__":
    print("Hello World")
    repeat_hello(somename="Shaina", n_times=6)
    hello_name("Shaina")

    list_of_names = ("Shaina", "Anand", "Jack", "John")
    for name in list_of_names:
        hello_name(name)


    number_list = [1,2,3,4,5]
    print(number_list)
    for num in number_list:
        print(num)

    print_even_up_to_number(21)
