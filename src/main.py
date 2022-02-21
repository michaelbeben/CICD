#start fizzbuzz function, prints fizz for all numbers divisible by 3, buzz for all numbers divisible by 5, and fizzbuzz for all numbers divisible by 3 and 5
def fizzbuzz(number):
    for i in range(1, number):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FIZZBUZZ")
        elif (i % 3 == 0):
            print("FIZZ")
        elif (i % 5 == 0):
            print("BUZZ")

if __name__ == "__main__":
    fizzbuzz(100)

