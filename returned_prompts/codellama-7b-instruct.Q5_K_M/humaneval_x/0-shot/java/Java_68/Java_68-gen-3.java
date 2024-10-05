        List<Integer> res = new ArrayList<>();
        if (arr == null || arr.size() == 0) return res;

        int min = Integer.MAX_VALUE;
        int index = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < min) {
                min = arr.get(i);
                index = i;
            }
        }

        res.add(min);
        res.add(index);
        return res;
    }
}

