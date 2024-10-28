    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> map = new HashMap<>();
        if (test.isEmpty()) {
            return map;
        }
        String[] words = test.split(" ");
        int maxCount = 0;
        for (String word : words) {
            Integer count = map.get(word);
            if (count == null) {
                count = 1;
            } else {
                count++;
            }
            map.put(word, count);
            if (count > maxCount) {
                maxCount = count;
            }
        }
        List<String> result = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() == maxCount) {
                result.add(entry.getKey());
            }
        }
        Map<String, Integer> finalMap = new HashMap<>();
        for (String key : result) {
            finalMap.put(key, maxCount);
        }
        return finalMap;
    } 














