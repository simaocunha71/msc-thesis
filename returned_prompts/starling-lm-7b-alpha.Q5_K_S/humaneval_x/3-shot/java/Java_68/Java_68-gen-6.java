        int min_value = Integer.MAX_VALUE;
        int index = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < min_value) {
                min_value = arr.get(i);
                index = i;
            }
        }
        return new ArrayList<>(Collections.singletonList(min_value)).add(index);
    }
}

