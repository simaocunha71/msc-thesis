        Map<String, Integer> result = new HashMap<>();

        for (String s : test.split(" ")) {
            if (result.containsKey(s)) {
                result.put(s, result.get(s) + 1);
            } else {
                result.put(s, 1);
            }
        }
        return result;
    }
}

