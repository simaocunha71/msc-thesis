        List<Integer> result = new ArrayList<>();
        int[] t = new int[n + 1];
        t[1] = 3;
        result.add(t[1]);
        for (int i = 2; i < t.length; i++) {
            if (i % 2 == 0) {
                t[i] = 1 + i / 2;
            } else {
                t[i] = t[i - 1] + t[i - 2] + t[i + 1];
            }
            result.add(t[i]);
        }
        return result;
    }
}

