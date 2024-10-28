        Map<String, Integer> result = new HashMap<>();
        String[] parts = test.split(" ");
        for (String part : parts) {
            Integer count = result.get(part);
            if (count == null) {
                result.put(part, 1);
            } else {
                result.put(part, count + 1);
            }
        }
        return result;
    }
}

