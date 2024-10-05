        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            result.add(n);
            if (n % 2 == 0) n++;
            n += 2;
        }
        return result;
    }
}