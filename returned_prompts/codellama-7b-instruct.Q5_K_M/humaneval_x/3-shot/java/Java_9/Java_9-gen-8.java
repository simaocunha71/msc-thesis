        List<Integer> result = new ArrayList<>();
        int current_max = numbers.get(0);
        result.add(current_max);

        for (int i = 1; i < numbers.size(); i++) {
            int current_number = numbers.get(i);
            if (current_number > current_max) current_max = current_number;
            result.add(current_max);
        }
        return result;
    }
}

