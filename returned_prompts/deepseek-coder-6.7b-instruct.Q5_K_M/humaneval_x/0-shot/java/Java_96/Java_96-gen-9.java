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

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }
}

The function isPrime checks if a number is prime by dividing it by every integer less than its square root (as a number cannot be divided evenly by an integer larger than its square root).

The function countUpTo checks every integer less than the input number and adds it to the list of prime numbers if it is prime. It returns this list.

Note: The function does not include 0 and 1 as prime numbers, as per the definition of prime numbers.
*/

//Test Cases:

// countUpTo(5) => [2,3]
// countUpTo(11) => [2,3,5,7]
// countUpTo(0) => []
// countUpTo(20) => [2,3,5,7,11,13,17,19]
// countUpTo(1) => []
// countUpTo(18) => [2,3,5,7,11,13,17]

//The above code will run as expected for these test cases.

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.countUpTo(5));
        System.out.println(sol.countUpTo(11));
        System.out.println(sol.countUpTo(0));
        System.out.println(sol.countUpTo(20));
        System.out.println(sol.countUpTo(1));
        System.out.println(