    int largestPrime = Integer.MIN_VALUE;
    for (int num : lst) {
        if (isPrime(num) && num > largestPrime) {
            largestPrime = num;
        }
    }

    return sumOfDigits(largestPrime);
}

private boolean isPrime(int num) {
    if (num <= 1) {
        return false;
    }

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}

private int sumOfDigits(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }

    return sum;
}

}

I'm not sure why this isn't working. It seems to be correct according to the problem statement.

A: If there is no largest prime number in the list, then largestPrime will remain as Integer.MIN_VALUE which is less than 0. In the line 
if (isPrime(num) && num > largestPrime) 

it will never be true because Integer.MIN_VALUE is less than 0.
You can add a check at the beginning of the method to return 0 if there are no prime numbers in the list. 
public int skjkasdkd(List<Integer> lst) {
    int largestPrime = Integer.MIN_VALUE;
    boolean primeExists = false;

    for (int num : lst) {
        if (isPrime(num) && num > largestPrime) {
            largestPrime = num;
            primeExists = true;
        }
    }

    if (!primeExists) {
        return 0;
    }

    return sumOfDigits(largestPrime);
}

This way, if there are no prime numbers in the list, the method will return 0 as expected.

A: This code assumes that the input list always contains at least one prime number. However, in some cases, the list might