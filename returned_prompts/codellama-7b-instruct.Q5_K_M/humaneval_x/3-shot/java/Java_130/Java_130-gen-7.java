        List<Integer> result = new ArrayList<>();
        result.add(0);
        result.add(3);
        result.add(1);
        for (int i = 2; i <= n; i++) {
            int n1 = result.get(i - 1);
            int n2 = result.get(i - 2);
            int n3 = result.get(i - 3);
            int sum = n1 + n2 + n3;
            result.add(sum);
        }
        return result;
    }
}

