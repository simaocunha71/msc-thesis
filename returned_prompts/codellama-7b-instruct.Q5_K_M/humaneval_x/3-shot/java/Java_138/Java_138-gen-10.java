        for (int i = 2; i < n / 2; i += 2) {
            int sum = i + i + i + i;
            if (sum == n) return true;
        }
        return false;
    }
}

