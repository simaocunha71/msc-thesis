        int count = 0;
        for  (int i = 2; i <= a && count < 4; i++) {
            while  (a % i == 0) {
                count++;
                a /= i;
            }
        }
        return count == 3 && a == 1;
     }
}

