        for (int i = 2; i <= n; i += 2) {
            int sum = 0;
            for (int j = 2; j <= n; j += 2) {
                sum += j;
                if (sum == n) return true;
                if (sum > n) break;
            }
        }
        return false;
    }
}

