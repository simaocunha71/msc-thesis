        int count = 0;
        for(int i = 2; i < a; i++){
            if(a % i == 0){
                while(a % i == 0){
                    a = a / i;
                    count++;
                }
                if(isPrime(i) == false){
                    return false;
                }
            }
        }
        if(a != 1 && isPrime(a) == false){
            return false;
        }

        if(count > 2){
            return false;
        }
        return true;
    }

    public boolean isPrime(int n)
    {
        if ( n == 2 || n == 3 ) return true;
        if ( n == 1 || n % 2 == 0 ) return false;
        for ( int i = 3; i * i <= n; i += 2 )
            if ( n % i == 0 )
                return false;
        return true;
    }

    public static void main (String[] args) throws java.lang.Exception
    {
        Solution s = new Solution();
        System.out.println(s.isMultiplyPrime(30)); //true
        System.out.println(s.isMultiplyPrime(31)); //false
    }
}

This is a java solution for the problem.
First, we find all prime factors of the number. If the number is not a prime number, return false. If the number is a prime number, increment the count. If the count is more than 2, return false. Otherwise, return true.
The isPrime function checks if a number is prime or not.
The main function tests the isMultiplyPrime function with the examples in the problem statement.
The time complexity of the solution is O(sqrt(n)).
*/

//END CODE

//END SOLUTION

//END SUBMISSION



































































