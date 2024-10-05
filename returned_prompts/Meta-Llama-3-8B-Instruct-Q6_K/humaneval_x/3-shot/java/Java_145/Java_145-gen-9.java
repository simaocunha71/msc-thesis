        List<Integer> result = new ArrayList<>();
        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>();
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            int digitSum = getDigitSum(num);
            entries.add(new AbstractMap.SimpleEntry<>(digitSum, i));
        }
        Collections.sort(entries, new Comparator<Map.Entry<Integer, Integer>>() {
            public int compare(Map.Entry<Integer, Integer> e1, Map.Entry<Integer, Integer> e2) {
                if (e1.getKey().equals(e2.getKey())) {
                    return e1.getValue().compareTo(e2.getValue());
                } else {
                    return e1.getKey().compareTo(e2.getKey());
                }
            }
        });
        for (Map.Entry<Integer, Integer> entry : entries) {
            result.add(nums.get(entry.getValue()));
        }
        return result;
    }

    private int getDigitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

