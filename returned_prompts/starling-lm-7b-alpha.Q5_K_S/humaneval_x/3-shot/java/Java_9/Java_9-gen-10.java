        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < numbers.size(); i++) {
            if (numbers.get(i) > max) {
                max = numbers.get(i);
            }
            result.add(max);
        }
        return result;
    }
}

