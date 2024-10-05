        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            if (i != numbers.size() - 1) {
                result.add(delimiter);
            }
        }
        return result;
    }
}

