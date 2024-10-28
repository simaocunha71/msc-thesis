        int c = 0;

        for(int i = 0; i < num.length(); i++) {
            if(num.charAt(i) == '0' || num.charAt(i) == '1' || num.charAt(i) == '2' || num.charAt(i) == '3' || num.charAt(i) == '4' || num.charAt(i) == '5' || num.charAt(i) == '6' || num.charAt(i) == '7' || num.charAt(i) == '8' || num.charAt(i) == '9') {
                if(isPrime(Integer.parseInt(String.valueOf(num.charAt(i)))))
                    c++;
            } else if(num.charAt(i) == 'A') {
                if(isPrime(11))
                    c++;
            } else if(num.charAt(i) == 'B') {
                if(isPrime(13))
                    c++;
            } else if(num.charAt(i) == 'C') {
                if(isPrime(17))
                    c++;
            } else if(num.charAt(i) == 'D') {
                if(isPrime(19))
                    c++;
            } else if(num.charAt(i) == 'E') {
                if(isPrime(23))
                    c++;
            } else if(num.charAt(i) == 'F') {
                if(isPrime(29))
                    c++;
            }
        }
        return c;
    }

    public boolean isPrime(int n) {
        if(n % 2 == 0)
            return false;
        for(int i = 3; i * i <= n; i += 2) {
            if(n % i == 0)
                return false;
        }
        return true;
    }
}
























