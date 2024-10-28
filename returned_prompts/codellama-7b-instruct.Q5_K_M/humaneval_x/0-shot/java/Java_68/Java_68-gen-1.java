        List<Integer> list = new ArrayList<>();
        if (arr.size() == 0) {
            return list;
        }

        int min = Integer.MAX_VALUE;
        int index = 0;
        int i = 0;
        for (; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < min) {
                min = arr.get(i);
                index = i;
            }
        }

        list.add(min);
        list.add(index);
        return list;
    }
}
