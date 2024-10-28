        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            int max = numbers.get(i);
            for (int j = i; j < numbers.size(); j++) {
                if (numbers.get(j) > max) max = numbers.get(j);
            }
            result.add(max);
        }
        return result;
    }
}

