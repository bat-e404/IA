def factorial(num):
    numFactorial = 1
    
    while(num > 0):
        numFactorial *= num
        num -= 1
    
    return numFactorial

print(factorial(4))
