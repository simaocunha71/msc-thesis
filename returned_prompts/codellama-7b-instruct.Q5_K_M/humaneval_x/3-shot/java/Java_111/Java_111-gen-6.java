        Map<String, Integer> hist = new HashMap<String, Integer>();

        String[] letters = test.split(" ");

        for (String letter : letters) {
            if (hist.containsKey(letter)) {
                hist.put(letter, hist.get(letter) + 1);
            } else {
                hist.put(letter, 1);
            }
        }

        return hist;
    }
}

