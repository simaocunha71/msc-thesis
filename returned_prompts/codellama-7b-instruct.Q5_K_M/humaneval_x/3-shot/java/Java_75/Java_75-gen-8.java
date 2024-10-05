        for (int i = 2; i < a; i++) {
            if (a % i == 0) {
                int b = a / i;
                for (int j = 2; j < b; j++) {
                    if (b % j == 0) {
                        return false;
                    }
                }
                return true;
            }
        }
        return false;
    }
}

