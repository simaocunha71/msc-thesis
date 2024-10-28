        int[] factors = new int[a];
        int count = 0;
        for (int i = 1; i < 100; i++) {
            if (a % i == 0) {
                factors[count] = i;
                count += 1;
            }
        }
        if (count != 3) return false;
        for (int i = 0; i < count; i++) {
            for (int j = i + 1; j < count; j++) {
                for (int k = j + 1; k < count; k++) {
                    if (factors[i] * factors[j] * factors[k] == a) return true;
                }
            }
        }
        return false;
    }
}

