        int count = 0;
        for  (int i = 2; i <= a; i++) {
            while  (a % i == 0) {
                count++;
                a /= i;
            }
        }
        return count == 3;
     }
}

