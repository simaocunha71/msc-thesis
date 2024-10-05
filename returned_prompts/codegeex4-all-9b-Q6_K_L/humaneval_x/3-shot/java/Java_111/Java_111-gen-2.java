        Map<String, Integer> result = new HashMap<>();
        String[] letters = test.split(" ");

        for (String letter : letters) {
            if (result.containsKey(letter)) {
                int count = result.get(letter);
                result.put(letter, count + 1);
            } else {
                result.put(letter, 1);
            }
        }
        return result;
    }
}

