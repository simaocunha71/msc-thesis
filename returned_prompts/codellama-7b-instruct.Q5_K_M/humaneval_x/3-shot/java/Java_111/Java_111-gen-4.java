        Map<String, Integer> result = new HashMap<>();

        if (test.isEmpty()) return result;

        String[] letters = test.split(" ");
        Map<String, Integer> temp = new HashMap<>();

        for (String letter : letters) {
            if (temp.containsKey(letter)) {
                temp.put(letter, temp.get(letter) + 1);
            } else {
                temp.put(letter, 1);
            }
        }

        for (Map.Entry<String, Integer> entry : temp.entrySet()) {
            if (entry.getValue() > result.get(entry.getKey())) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}

