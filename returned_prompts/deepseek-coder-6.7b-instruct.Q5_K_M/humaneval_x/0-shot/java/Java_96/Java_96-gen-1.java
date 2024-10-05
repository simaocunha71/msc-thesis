        List<Integer> primeNumbers = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primeNumbers.add(i);
            }
        }
        return primeNumbers;
    }
    
    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

This Java solution defines a class Solution with a method countUpTo that takes an integer n as input and returns a list of prime numbers less than n. The method isPrime is used to check whether a number is prime or not.
*/

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.countUpTo(5));
        System.out.println(solution.countUpTo(11));
        System.out.println(solution.countUpTo(0));
        System.out.println(solution.countUpTo(20));
        System.out.println(solution.countUpTo(1));
        System.out.println(solution.countUpTo(18));
    }
}

/*
Output:
[2, 3]
[2, 3, 5, 7]
[]
[2, 3, 5, 7, 11, 13, 17, 19]
[]
[2, 3, 5, 7, 11, 13, 17]
*/


/*
