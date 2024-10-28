        List<Integer> result = new ArrayList<>();
        int first = 1;
        int second = 3;
        int third = 2;
        int current;
        result.add(first);
        result.add(second);
        result.add(third);

        for (int i = 0; i < n; i++) {
            current = first + second + third;
            first = second;
            second = third;
            third = current;
            result.add(current);
        }
        return result;
    }
}

