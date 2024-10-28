        int n = arr.size();
        int[] odd = new int[n];
        int[] even = new int[n];
        Arrays.fill(odd, -1);
        Arrays.fill(even, -1);

        for (int i = 0; i < n; i++) {
            int val = arr.get(i);
            if (i > 0 && i < n - 1 && val % 2 == 1) {
                if (odd[i - 1] == -1) odd[i - 1] = val;
                else odd[i - 1] = Math.min(odd[i - 1], val);
                if (odd[i + 1] == -1) odd[i + 1] = val;
                else odd[i + 1] = Math.min(odd[i + 1], val);
            } else if (i == 0 && val % 2 == 1) odd[0] = val;
            else if (i == n - 1 && val % 2 == 1) odd[n - 1] = val;
            if (i % 2 == 0) {
                if (even[i] == -1) even[i] = val;
                else even[i] = Math.min(even[i], val);
            } else {
                if (even[i - 1] == -1) even[i - 1] = val;
                else even[i - 1] = Math.min(even[i - 1], val);
                if (even[i + 1] == -1) even[i + 1] = val;
                else even[i + 1] = Math.min(even[i + 1], val);
            }
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 && arr.get(0) % 2 == 0) {
                count++;
                continue;
            }
            if (i == n - 1 && arr.get(n - 1)