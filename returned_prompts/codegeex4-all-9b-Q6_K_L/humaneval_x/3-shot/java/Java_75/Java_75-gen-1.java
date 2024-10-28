        for (int i = 2; i <= Math.sqrt(a); i++) {
            if (a % i == 0) {
                int count = 0;
                while (a % i == 0) {
                    count++;
                    a /= i;
                }

                if (count > 1) return false;
            }
        }
        return a == 1;
    }
}

