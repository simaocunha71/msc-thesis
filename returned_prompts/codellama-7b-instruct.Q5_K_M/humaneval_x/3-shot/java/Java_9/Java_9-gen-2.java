        List<Integer> result = new ArrayList<>();
        int current_max = numbers.get(0);

        for (int i = 0; i < numbers.size(); i++) {
            if (numbers.get(i) > current_max) current_max = numbers.get(i);
            result.add(current_max);
        }
        return result;
    }
}

