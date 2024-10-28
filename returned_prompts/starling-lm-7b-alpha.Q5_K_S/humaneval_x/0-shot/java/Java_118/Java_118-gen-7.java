    String[] vowels = {"a", "e", "i", "o", "u"};
    char[] wordChar = word.toCharArray();

    int min = wordChar.length;
    char result = ' ';

    for (int i = 0; i < wordChar.length; i++) {
        if (vowels.length > 0 && !vowels[0].equals("")) {
            for (int j = 0; j < vowels.length; j++) {
                if (wordChar[i] == vowels[j].charAt(0)) {
                    if (i > 0 && wordChar[i - 1] != '*') {
                        if (i < min) {
                            min = i;
                            result = vowels[j].charAt(0);
                        }
                    } else if (i < min) {
                        min = i;
                        result = vowels[j].charAt(0);
                    }
                }
            }
        }
        wordChar[i] = "*";
    }

    return result == ' ' ? "" : String.valueOf(result);
    }
}































































































































































































































