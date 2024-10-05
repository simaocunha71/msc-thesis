        int count = 0;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = i * i - i + 1;
            for (int j = i + 1; j < n; j++) {
                if (a[i] + a[j] % 3 == 0) {
                    for (int k = j + 1; k < n; k++) {
                        if (a[j] + a[k] % 3 == 0) {
                            count += 1;
                        }
                    }
                }
            }
        }
        return count;
    }
}

