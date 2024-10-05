        Map<String, Integer> result = new HashMap<>();
        Map<String, Integer> counter = new HashMap<>();
        for (char c : test.toCharArray()) {
            counter.put(String.valueOf(c), counter.getOrDefault(String.valueOf(c), 0) + 1);
        }
        result.putAll(counter);
        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        // test code here
    }
}


```