        Map<String, Integer> result = new HashMap<>();
        for (char c : test.toCharArray()) {
            int count = result.getOrDefault(c + "", 0);
            result.put(c + "", count + 1);
        }
        return result;
    }
}

