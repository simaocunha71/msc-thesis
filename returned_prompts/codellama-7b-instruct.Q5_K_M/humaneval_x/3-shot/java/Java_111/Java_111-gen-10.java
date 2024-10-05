        Map<String, Integer> result = new HashMap<>();
        String[] letters = test.split(" ");
        for (String letter : letters) {
            if (result.containsKey(letter)) {
                result.put(letter, result.get(letter) + 1);
            } else {
                result.put(letter, 1);
            }
        }
        return result;
    }
}

