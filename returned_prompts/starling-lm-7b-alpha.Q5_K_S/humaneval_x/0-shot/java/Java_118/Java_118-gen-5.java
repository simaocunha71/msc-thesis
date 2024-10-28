        char[] arr = new char[] {'a', 'e', 'i', 'o', 'u'};
        int[] index = new int[26];
        for (int i = 0; i < 26; i++) {
            index[i] = -1;
        }

        for (int i = 0; i < word.length(); i++) {
            if (Arrays.asList(arr).contains(Character.toString(word.charAt(i)))) {
                index[word.charAt(i) - 'a'] = i;
            }
        }

        int max = 0;
        int pos = -1;

        for (int i = 0; i < word.length(); i++) {
            if (Character.isLetter(word.charAt(i))) {
                if (index[word.charAt(i) - 'a'] != -1 && index[word.charAt(i) - 'a'] >= max) {
                    max = index[word.charAt(i) - 'a'];
                    pos = i;
                }
            }
        }

        return word.charAt(pos) == word.charAt(word.length() - 1) ? "" : Character.toString(word.charAt(pos));
    }
}








































































































































































































