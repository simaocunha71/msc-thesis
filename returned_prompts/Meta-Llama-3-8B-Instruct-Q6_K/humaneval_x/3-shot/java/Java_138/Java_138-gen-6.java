        for (int i = 2; i <= n; i++) {
            int sum = 0;
            for (int j = 2; j <= n; j++) {
                if (i + j <= n) {
                    sum += i + j;
                    if (sum == n) return true;
                } else {
                    break;
                }
            }
        }
        return false;
    }
}

