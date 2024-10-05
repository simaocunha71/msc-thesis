public String removeVowels(String text) {
        String[] vowels = new String[] {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"};
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            if (!Arrays.asList(vowels).contains(String.valueOf(text.charAt(i)))) {
                result += text.charAt(i);
            }
        }
        return result;
    }