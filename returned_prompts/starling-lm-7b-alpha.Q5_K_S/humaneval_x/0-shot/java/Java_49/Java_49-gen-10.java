        if(n < 0) {
            return modp(-n, p);
        }
        if(n == 0) {
            return 1;
        }
        int res = 1;
        while(n > 0) {
            if((n & 1) == 1) {
                res = (int)(((long)res * ((long)p % 1000000007)) % 1000000007);
            }
            n >>= 1;
            p = (int)(((long)p * ((long)p % 1000000007)) % 1000000007);
        }
        return res;
    }

    public boolean isPrime(int n) {
        if (n == 2) {
            return true;
        }
        if (n < 2 || n % 2 == 0) {
            return false;
        }
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public boolean isPowerOfTwo(int n) {
        return (int)(Math.pow(2, Integer.numberOfTrailingZeros(n))) == n;
    }
    /**
    >>> isPowerOfTwo(16)
    true
    >>> isPowerOfTwo(30)
    false
    >>> isPowerOfTwo(0)
    false
    >>> isPowerOfTwo(1)
    true
    >>> isPowerOfTwo(3)
    false
    */

    public int gcd(int a, int b) {
        if(a == 0) {
            return b;
        }
        if(b == 0) {
            return a;
        }
        if(a > b) {
            return gcd(a % b, b);
        }
        return gcd(b % a, a);
    }

    public int findNthInArray(int[] arr,