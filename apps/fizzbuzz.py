def fizzBuzz(input):
    if input%3==0:
        if input%5==0:
           return "FizzBuzz"
        return "Fizz"
    if input%5==0:
        return "Buzz"
    return str(input)