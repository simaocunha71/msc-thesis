        Map<String, Integer> result = new HashMap<>();
        if (test.length() == 0) {
            return result;
        }

        int max = 0;
        char maxChar = ' ';
        char[] arr = test.toCharArray();
        for (char c : arr) {
            if (result.containsKey(String.valueOf(c))) {
                int count = result.get(String.valueOf(c));
                result.put(String.valueOf(c), ++count);
                if (count > max) {
                    max = count;
                    maxChar = c;
                } else if (count == max) {
                    result.put(String.valueOf(c), count);
                }
            } else {
                result.put(String.valueOf(c), 1);
                if (1 > max) {
                    max = 1;
                    maxChar = c;
                } else if (1 == max) {
                    result.put(String.valueOf(c), 1);
                }
            }
        }
        result.put(String.valueOf(maxChar), max);
        return result;
    }
}
































































































































































































































