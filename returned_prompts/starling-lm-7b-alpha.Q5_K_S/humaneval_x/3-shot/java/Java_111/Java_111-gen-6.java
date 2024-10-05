        Map<String, Integer> result = new HashMap<>();
        for (String s : test.split(" ")) {
            result.put(s, result.getOrDefault(s, 0) + 1);
        }
        return result;
    }
}

