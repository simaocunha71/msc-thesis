        List<Integer> result = new ArrayList<>();
        if (arr == null || arr.size() == 0) return result;

        int min = Integer.MAX_VALUE;
        int minIndex = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < min) {
                min = value;
                minIndex = i;
            }
        }

        if (minIndex != Integer.MAX_VALUE) {
            result.add(min);
            result.add(minIndex);
        }

        return result;
    }
}

