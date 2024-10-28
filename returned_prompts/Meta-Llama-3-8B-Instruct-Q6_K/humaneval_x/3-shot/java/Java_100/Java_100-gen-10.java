        List<Integer> result = new ArrayList<>();
        int i = 1;
        while (i <= n) {
            if (i % 2 == 0) {
                result.add(i);
            } else {
                result.add(i + 1);
            }
            i += 2;
        }
        return result;
    }
}

