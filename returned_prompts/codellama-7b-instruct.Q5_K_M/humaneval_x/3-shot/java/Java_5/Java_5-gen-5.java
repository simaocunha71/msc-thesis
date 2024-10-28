        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < numbers.size(); i++) {
            if (i != 0) result.add(delimiter);
            result.add(numbers.get(i));
        }
        return result;
    }
}

