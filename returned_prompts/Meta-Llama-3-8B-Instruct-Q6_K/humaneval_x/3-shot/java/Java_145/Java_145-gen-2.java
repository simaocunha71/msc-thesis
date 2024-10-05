        List<Integer> result = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            int sum = 0;
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            map.put(sum, i);
        }
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            int num = nums.get(map.get(sum));
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            result.add(nums.get(map.get(sum)));
            nums.set(map.get(sum), nums.get(nums.size() - 1));
            map.put(sum, nums.size() - 1);
        }
        return result;
    }
}  