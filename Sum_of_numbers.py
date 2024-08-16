

def sum_of_numbers(num):
    output = 0
    for i in range(1,num+1):
        output += i
    return output


if __name__ == "__main__":
    print("Hello World")
    for i in range(1,11):
      print(f"num = {1},  sum_of_numbers(1) = {sum_of_numbers(i)}")