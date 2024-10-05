        int result = 0;
        int n = arr.size();
        for (int i = 0; i < n / 2; i++) {
            if (arr.get(i) != arr.get(n - 1 - i)) {
                result += 1;
            }
        }
        if (n % 2 == 1) {
            result += 1;
        }
        return result;
    }
}

