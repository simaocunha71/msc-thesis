        boolean isPrime = true;
        for(int i = 2; i <= Math.sqrt(a); i++) {
            if(a % i == 0) {
                isPrime = false;
                break;
            }
        }
        if(isPrime) {
            for(int i = 2; i <= Math.sqrt(a); i++) {
                if(a % i == 0) {
                    for(int j = i; j <= Math.sqrt(a); j++) {
                        if(a % j == 0 && isPrime(j) && isPrime(i)) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;

    }

    private boolean isPrime(int num) {
        for(int i = 2; i <= Math.sqrt(num); i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
S:
The isMultiplyPrime method checks if the given number 'a' is the multiplication of 3 prime numbers. It first checks if 'a' is prime. If 'a' is not prime, it then checks for every number 'i' less than or equal to the square root of 'a', if 'a' is divisible by 'i'. If 'a' is divisible by 'i', it then checks for every number 'j' less than or equal to the square root of 'a', if 'a' is divisible by 'j' and both 'i' and 'j' are prime. If such 'i' and 'j' are found, the method returns true. If no such 'i' and 'j' are found, the method returns false.

The isPrime method checks if a given number 'num' is prime. It does this by checking for every number 'i' less than or equal to the square root of 'num', if 'num' is divisible by 'i'. If 'num' is divisible by 'i', the method returns false. If 'num' is not divisible by any of the numbers from 2 to its square root, the method returns true.

This solution has a time complexity of O(sqrt(a)^2) and a space complexity of O(1). The space complexity is O(1) because it only uses a constant amount of space to store the variables. The time complexity is O(sqrt(a)^2) because it checks every number less than or equal to the square root of 'a' twice. The first loop in