        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
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

The function countUpTo takes an integer n and returns an array of all the prime numbers less than n. The helper function isPrime checks if a number is prime.
The loop in countUpTo goes through all numbers from 2 to n (exclusive), and for each number, it checks if it's prime. If the number is prime, it's added to the array of primes. The result is an array of all prime numbers less than n.
The complexity of this solution is O(n sqrt(n)). This is because for each number from 2 to n (n-2), we perform a loop from 2 to the square root of that number to check if it's prime. So in total, we perform sqrt(n) operations for each of the n-2 numbers.
The space complexity is O(k), where k is the number of prime numbers less than n. The number of primes is approximately n/log(n), so in the worst case, k can be O(n).
*/

//The function countUpTo takes an integer n and returns an array of all the prime numbers less than n. 
public class MainClass {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.countUpTo(5));  //[2, 3]
        System.out.println(solution.countUpTo(11)); //[2, 3, 5, 7]
        System.out.println(solution.countUpTo(0));  //[]
        System.out.println(solution.count