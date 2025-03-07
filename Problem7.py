#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime
from NumberTests import findNthPrime

def main():
    nthPrime = findNthPrime(10001)
    print(nthPrime)

if __name__ == '__main__':
  main()