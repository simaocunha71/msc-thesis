        Collections.sort(numbers);
        int min = Integer.MAX_VALUE;
        int min_index = 0;
        for (int i = 0; i < numbers.size(); i++) {
            int diff = (int) (numbers.get(i) - numbers.get(i - 1));
            if (diff < min) {
                min = diff;
                min_index = i;
            }
        }
        return Arrays.asList(numbers.get(min_index - 1), numbers.get(min_index));
    }
}

