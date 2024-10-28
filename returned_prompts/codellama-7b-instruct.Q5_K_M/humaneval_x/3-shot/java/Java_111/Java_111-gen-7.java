        Map<String, Integer> result = new HashMap<>();
        for (String letter : test.split(" ")) {
            if (result.containsKey(letter)) {
                result.put(letter, result.get(letter) + 1);
            } else {
                result.put(letter, 1);
            }
        }
        return result;
    }
}

