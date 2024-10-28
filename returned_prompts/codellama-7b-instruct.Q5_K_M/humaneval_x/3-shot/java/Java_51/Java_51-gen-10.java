        String vowels = "aeiou";
        char[] result = new char[text.length()];
        int j = 0;

        for (int i = 0; i < text.length(); i++) {
            if (vowels.indexOf(text.charAt(i)) == -1) {
                result[j] = text.charAt(i);
                j++;
            }
        }
        return new String(result, 0, j);
    }
}

