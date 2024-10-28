        Map<String, Integer> result = new HashMap<>();
        for (int i = 0; i < test.length(); i++) {
            String letter = test.substring(i, i + 1);
            if (result.containsKey(letter)) {
                result.put(letter, result.get(letter) + 1);
            } else {
                result.put(letter, 1);
            }
        }
        return result;
    }
}

