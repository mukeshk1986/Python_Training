# without parameter example
def fun():
    print("Welcome to coding!")

# with parameter example
def say_hello(name):
    print(f"hello {name}")

def add_2num(num1, num2):
    sum_2 = num1 +num2
    return sum_2


def evenOdd(num):
    if (num % 2 == 0):
        return "Even"
    else:
        return "Odd"



def myfun(x, y=50):
    print("x: ", x)
    print("y: ", y)



def student (fname, name):
    print (fname, name)


def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)


    
    




if __name__ == "__main__"    :
    # fun()
    # say_hello("Mukesh")
    # num1 = 10 
    # num2 = 14
    # final_sum_result = add_2num(num1, num2)
    # print('The result is ', final_sum_result)
    # print(evenOdd(16))
    # print(evenOdd(7))
    # myfun(10)
    myfun(10,30)
    student (fname='Geeks', name='practice')
    student (name='practice', fname='Geeks')
    print("case-1:")
    nameAge("silpa", 36)

    print("\nCase-2:")
    nameAge(36, "silpa")