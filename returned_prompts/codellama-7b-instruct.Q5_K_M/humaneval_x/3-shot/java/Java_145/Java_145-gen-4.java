        List<Integer> result = new ArrayList<>();

        Map<Integer, Integer> index_map = new HashMap<>();
        Map<Integer, Integer> sum_map = new HashMap<>();

        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            sum_map.put(num, sum(num));
            index_map.put(num, i);
        }

        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(sum_map.entrySet());

        Collections.sort(list, new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                if (o1.getValue() == o2.getValue()) {
                    return index_map.get(o1.getKey()).compareTo(index_map.get(o2.getKey()));
                }
                return o1.getValue().compareTo(o2.getValue());
            }
        });

        for (Map.Entry<Integer, Integer> entry : list) {
            result.add(entry.getKey());
        }

        return result;
    }

    private int sum(int num) {
        int result = 0;
        while (num > 0) {
            result += num % 10;
            num /= 10;
        }
        return result;
    }
}

