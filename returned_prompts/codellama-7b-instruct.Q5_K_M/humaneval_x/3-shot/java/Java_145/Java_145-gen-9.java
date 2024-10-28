        List<Integer> result = new ArrayList<>(nums.size());
        Map<Integer, List<Integer>> sum_map = new HashMap<>();

        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (char c : Integer.toString(nums.get(i)).toCharArray()) {
                sum += Character.getNumericValue(c);
            }
            if (sum_map.containsKey(sum)) {
                sum_map.get(sum).add(nums.get(i));
            } else {
                List<Integer> item_list = new ArrayList<>();
                item_list.add(nums.get(i));
                sum_map.put(sum, item_list);
            }
        }

        List<Integer> sorted_sums = new ArrayList<>(sum_map.keySet());
        sorted_sums.sort((x, y) -> Integer.compare(x, y));
        for (int sum : sorted_sums) {
            List<Integer> items = sum_map.get(sum);
            Collections.sort(items, (x, y) -> Integer.compare(x, y));
            result.addAll(items);
        }
        return result;
    }
}

