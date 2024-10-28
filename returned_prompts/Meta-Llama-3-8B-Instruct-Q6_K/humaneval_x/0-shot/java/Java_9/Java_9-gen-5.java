    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        if (numbers.isEmpty()) {
            return result;
        }
        int max = numbers.get(0);
        result.add(max);
        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) > max) {
                max = numbers.get(i);
            }
            result.add(max);
        }
        return result;
    }