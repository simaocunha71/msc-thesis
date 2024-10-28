        int primeCount = 0;
        for(int i = 2; i <= a; i++) {
            while(a % i == 0) {
                primeCount++;
                a /= i;
            }
        }
        return primeCount == 3;
     }
}

