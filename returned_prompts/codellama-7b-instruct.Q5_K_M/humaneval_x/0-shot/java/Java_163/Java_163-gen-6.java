        if (a < 0 || b < 0) {
            throw new IllegalArgumentException("Invalid input");
        }
        List<Integer> result = new ArrayList<Integer>();
        for (int i = a; i <= b; i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        return result;
    }
}
