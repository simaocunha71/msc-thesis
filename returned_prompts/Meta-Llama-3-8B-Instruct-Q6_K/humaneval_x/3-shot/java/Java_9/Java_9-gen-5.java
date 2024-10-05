        List<Integer> result = new ArrayList<>();
        int max = numbers.get(0);
        result.add(max);

        for (int i = 1; i < numbers.size(); i++) {
            int current_max = Math.max(max, numbers.get(i));
            result.add(current_max);
            max = current_max;
        }
        return result;
    }
}

