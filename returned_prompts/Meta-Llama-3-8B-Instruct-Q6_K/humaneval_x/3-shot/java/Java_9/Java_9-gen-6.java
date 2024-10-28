        List<Integer> result = new ArrayList<>();
        int max_so_far = numbers.get(0);
        result.add(max_so_far);
        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) > max_so_far) {
                max_so_far = numbers.get(i);
            }
            result.add(max_so_far);
        }
        return result;
    }
}

