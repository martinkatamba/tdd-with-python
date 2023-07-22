
def fizzBuzz(input):
    if input%3==0:
        if input%5==0:
           return "FizzBuzz"
        return "Fizz"
    if input%5==0:
        return "Buzz"
    return str(input)

def checkResult(input,output):
    result=fizzBuzz(input)
    assert result== output

def test_with_1_fizzBuzz():
    checkResult(1,"1")

def test_with_2_fizzBuzz():
    checkResult(2,"2")

def test_with_3_fizzBuzz():
    checkResult(3,"Fizz")

def test_with_5_fizzBuzz():
    checkResult(5,"Buzz")

def test_with_6_fizzBuzz():
    checkResult(6,"Fizz")

def test_with_10_fizzBuzz():
    checkResult(10,"Buzz")

def test_with_15_fizzBuzz():
    checkResult(15,"FizzBuzz")
