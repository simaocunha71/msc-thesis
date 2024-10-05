        Map<String, Integer> result = new HashMap<>();
        int max = 0;
        char[] ch = test.toCharArray();
        for (char c : ch) {
            if (!result.containsKey(String.valueOf(c))) {
                result.put(String.valueOf(c), 1);
            } else {
                int count = result.get(String.valueOf(c));
                result.put(String.valueOf(c), count + 1);
                if (count + 1 > max) {
                    max = count + 1;
                }
            }
        }
        if (result.size() == 1) {
            result.put(String.valueOf(ch[0]), max);
        } else {
            for (Map.Entry<String, Integer> entry : result.entrySet()) {
                if (entry.getValue() == max) {
                    System.out.print(entry.getKey());
                    System.out.print(':');
                    System.out.println(entry.getValue());
                }
            }
        }
        return result;
    }
}

















































































































































































































































