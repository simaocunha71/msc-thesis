        List<Integer> result = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (char c : String.valueOf(nums.get(i)).toCharArray()) {
                sum += Integer.parseInt(String.valueOf(c));
            }
            map.put(sum, i);
        }
        List<Integer> sorted = new ArrayList<>(map.keySet());
        Collections.sort(sorted);
        for (int i = 0; i < sorted.size(); i++) {
            result.add(nums.get(map.get(sorted.get(i))));
        }
        return result;
    }
}

