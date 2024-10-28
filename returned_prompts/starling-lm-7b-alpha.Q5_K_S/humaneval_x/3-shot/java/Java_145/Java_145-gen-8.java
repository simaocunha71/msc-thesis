        List<Integer> result = new ArrayList<>();
        List<Integer> digits = new ArrayList<>();
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (int d : String.valueOf(nums.get(i)).toCharArray()) {
                sum += Integer.parseInt(d);
            }
            result.add(sum);
            result.add(i);
            result.add(nums.get(i));
        }
        result.sort(Comparator.comparingInt(o -> o));
        result.sort(Comparator.comparingInt(o -> o));
        List<Integer> order = new ArrayList<>();
        for (int i = 0; i < nums.size(); i++) {
            order.add(result.get(2 * i + 2));
        }
        return order;
    }
}


```