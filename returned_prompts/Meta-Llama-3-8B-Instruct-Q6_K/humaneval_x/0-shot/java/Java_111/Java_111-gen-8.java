    import java.util.*;

    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> result = new HashMap<>();
        String[] words = test.split(" ");
        Map<String, Integer> countMap = new HashMap<>();

        for (String word : words) {
            if (result.isEmpty()) {
                result.put(word, 1);
            } else {
                if (countMap.containsKey(word)) {
                    countMap.put(word, countMap.get(word) + 1);
                } else {
                    countMap.put(word, 1);
                }
            }
        }

        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
            }
        }

        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() == maxCount) {
                result.put(entry.getKey(), maxCount);
            }
        }

        return result;
    } 
    