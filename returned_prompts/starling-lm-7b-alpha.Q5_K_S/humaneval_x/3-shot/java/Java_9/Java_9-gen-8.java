        List<Integer> result = new ArrayList<>();
        int max = numbers.get(0);

        result.add(max);
        for (int i = 1; i < numbers.size(); i++) {
            max = Math.max(numbers.get(i), max);
            result.add(max);
        }
        return result;
    }
}

