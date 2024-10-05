        Map<String, Integer> result = new HashMap<>();
        for (char c : test.toCharArray()) {
            result.put(c + "", result.getOrDefault(c + "", 0) + 1);
        }
        return result;
    }
}

