        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int num : nums) {
            int sum = sumDigits(num);

            if (!map.containsKey(sum)) {
                map.put(sum, new ArrayList<>());
            }
            map.get(sum).add(num);
        }

        List<Integer> result = new ArrayList<>();
        for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
            List<Integer> sorted = entry.getValue();
            Collections.sort(sorted, new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    int diff = sumDigits(o1) - sumDigits(o2);
                    if (diff == 0) {
                        return o1 - o2;
                    }
                    return diff;
                }
            });
            result.addAll(sorted);
        }
        return result;
    }

    public int sumDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

