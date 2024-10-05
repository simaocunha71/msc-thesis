        List<Integer> result = new ArrayList<>();
        if (arr.size() == 0) {
            return result;
        }
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < min) {
                min = arr.get(i);
                minIndex = i;
            }
        }
        result.add(min);
        result.add(minIndex);
        return result;
    }
}

