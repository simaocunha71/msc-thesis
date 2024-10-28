        Map<String, Integer> result = new HashMap<>();
        List<String> test_list = Arrays.asList(test.split(" "));

        for (String c : test_list) {
            if (result.containsKey(c)) {
                result.put(c, result.get(c) + 1);
            } else {
                result.put(c, 1);
            }
        }
        return result;
    }
}

