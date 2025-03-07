#Problem10.py
#Project Euler problem 10

from NumberTests import sumOfPrimes

def main():
    limit = 2000000
    result = sumOfPrimes(limit)
    print(result)


if __name__ == '__main__':
  main()