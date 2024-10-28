        String[] words = s.split(" ");
        StringBuilder[] sorted = new StringBuilder[words.length];

        for  (int i = 0; i < words.length; i++) {
            sorted[i] = new StringBuilder(words[i]);
            sorted[i].append(' ');
            char[] charArray = sorted[i].toString().toCharArray();
            Arrays.sort(charArray);
            sorted[i].setLength(0);
            for (char c : charArray) {
                sorted[i].append(c);
            }
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder str : sorted) {
            result.append(str);
        }

        return result.toString();
    }
}

