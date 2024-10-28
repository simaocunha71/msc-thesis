        StringBuilder result = new StringBuilder();
        String[] letters = message.split("");

        for (String letter : letters) {
            if (letter.matches("[a-zA-Z]")) {
                if (letter.matches("[aeiou]")) {
                    int pos = Arrays.asList("aeiou".split("")).indexOf(letter) + 2;
                    result.append(letter.toUpperCase());
                } else {
                    result.append(letter.toLowerCase());
                }
            } else {
                result.append(letter);
            }
        }
        return result.toString();
    }
}

