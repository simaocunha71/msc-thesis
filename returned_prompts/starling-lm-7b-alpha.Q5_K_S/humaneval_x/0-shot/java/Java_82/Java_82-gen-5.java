        for(int i = 0; i < string.length(); i++) {
            if(string.length() % 2 == 0) {
                return false;
            }
            if(isPrime(string.length())) {
                return true;
            }
        }
        return false;
    }

    public boolean isPrime(int num) {
        if(num == 1) {
            return false;
        }
        if(num == 2) {
            return true;
        }
        if(num % 2 == 0) {
            return false;
        }
        for(int i = 3; i * i <= num; i += 2) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.primeLength("Hello"));
        System.out.println(solution.primeLength("abcdcba"));
        System.out.println(solution.primeLength("kittens"));
        System.out.println(solution.primeLength("orange"));
    }
}























































































































































































































