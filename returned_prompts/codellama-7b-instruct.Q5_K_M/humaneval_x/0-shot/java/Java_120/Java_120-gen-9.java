        List<Integer> list = new ArrayList<>(k);
        for (int i = 0; i < k; i++) {
            int max = arr.get(i);
            for (int j = i + 1; j < k; j++) {
                if (arr.get(j) > max) {
                    max = arr.get(j);
                }
            }
            list.add(max);
        }
        return list;
    }
}
