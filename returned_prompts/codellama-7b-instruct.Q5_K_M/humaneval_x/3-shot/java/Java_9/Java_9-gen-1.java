        List<Integer> result = new ArrayList<>();
        int current_max = numbers.get(0);

        for (int i : numbers) {
            if (i > current_max) {
                current_max = i;
            }
            result.add(current_max);
        }
        return result;
    }
}

