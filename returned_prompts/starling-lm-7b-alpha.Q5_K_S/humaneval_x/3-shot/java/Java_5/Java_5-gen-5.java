        List<Integer> result = new ArrayList<>();
        result.add(numbers.get(0));
        for (int i = 1; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            result.add(delimiter);
        }
        return result;
    }
}

