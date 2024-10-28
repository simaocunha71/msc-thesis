        List<Integer> result = new ArrayList<>();
        int a_min = a;
        int a_max = b;
        if (a > b) {
            a_min = b;
            a_max = a;
        }

        for (int i = a_min; i <= a_max; i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        return result;
    }
}

