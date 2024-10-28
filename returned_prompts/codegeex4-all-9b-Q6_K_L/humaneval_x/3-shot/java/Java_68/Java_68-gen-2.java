        int min = Integer.MAX_VALUE;
        int index = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) <= min) {
                min = arr.get(i);
                index = i;
            }
        }
        if (index == -1) return new ArrayList<>();
        List<Integer> result = new ArrayList<>();
        result.add(min);
        result.add(index);
        return result;
    }
}

