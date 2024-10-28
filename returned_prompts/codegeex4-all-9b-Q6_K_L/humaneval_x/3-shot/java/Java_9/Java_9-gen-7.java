        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;

        for (int i : numbers) {
            if (i > max) {
                max = i;
            }
            result.add(max);
        }
        return result;

    }
}

