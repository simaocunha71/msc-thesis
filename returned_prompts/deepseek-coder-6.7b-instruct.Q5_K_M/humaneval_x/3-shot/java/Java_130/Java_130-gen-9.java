        List<Integer> result = new ArrayList<>();
        for(int i = 0; i <= n; i++) {
            result.add(triHelper(i));
        }
        return result;
    }

    private int triHelper(int n) {
        if(n == 1) {
            return 3;
        }
        if(n == 0) {
            return 1;
        }
        if(n % 2 == 0) {
            return 1 + n / 2;
        }
        return triHelper(n - 1) + triHelper(n - 2) + triHelper(n + 1);
    }
}

