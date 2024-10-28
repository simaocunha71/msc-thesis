        if (a < 100) {
            for (int i = 2; i <= 10; i++) {
                if (a % i == 0) {
                    int b = a / i;
                    if (b > 10) {
                        return false;
                    }

                    for (int j = 2; j <= 10; j++) {
                        if (b % j == 0) {
                            return false;
                        }
                    }
                    return true;
                }
            }
        }
        return false;
    }
}

