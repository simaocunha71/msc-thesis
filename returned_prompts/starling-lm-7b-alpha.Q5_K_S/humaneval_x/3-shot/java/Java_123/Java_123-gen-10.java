        List<Integer> result = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            int next = getNext(i);
            if (next % 2 != 0) result.add(next);
        }
        Collections.sort(result);
        return result;
    }

    private int getNext(int n) {
        if (n % 2 == 0) return n / 2;
        return 3 * n + 1;
    }
}

