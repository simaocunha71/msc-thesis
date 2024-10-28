        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size() - 1; i++) {
            result.add(numbers.get(i));
            result.add(delimiter);
        }
        if (numbers.size() > 0) {
            result.add(numbers.get(numbers.size() - 1));
        }
        return result;

    }
}

