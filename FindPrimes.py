def allPrimesUpTo(Num):
    primes = [2]
    for number in range(3,Num):
        sqrtNum = number**0.5
        for factor in primes:
            if number % factor ==0:
                #Not prime
                break
            if factor > sqrtNum:
                # It's prime!
                primes.append(number)
                break
    return primes

print(allPrimesUpTo(100))