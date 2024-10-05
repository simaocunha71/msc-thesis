        List<Integer> result = new ArrayList<>();
        int currentMax = numbers.get(0);
        result.add(currentMax);

        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) > currentMax) {
                currentMax = numbers.get(i);
            }
            result.add(currentMax);
        }

        return result;
    }
}

