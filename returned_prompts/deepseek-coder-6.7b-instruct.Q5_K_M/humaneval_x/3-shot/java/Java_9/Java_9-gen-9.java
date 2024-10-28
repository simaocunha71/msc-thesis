        List<Integer> result = new ArrayList<>();
        int max = numbers.get(0);
        result.add(max);

        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) > max) {
                max = numbers.get(i);
            }
            result.add(max);
        }
        return result;
     }
}

