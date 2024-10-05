        int index = -1;

        for (int i = word.length() - 1; i >= 0; i--) {
            if (word.charAt(i) == 'a' || word.charAt(i) == 'e' || word.charAt(i) == 'i' || word.charAt(i) == 'o' || word.charAt(i) == 'u') {
                index = i;
                break;
            }
        }

        if (index == -1) return "";

        int last_index = -1;

        for (int i = index - 1; i >= 0; i--) {
            if (word.charAt(i) == 'a' || word.charAt(i) == 'e' || word.charAt(i) == 'i' || word.charAt(i) == 'o' || word.charAt(i) == 'u') {
                last_index = i;
                break;
            }
        }

        if (last_index == -1) return "";

        return String.valueOf(word.charAt(last_index));
    }
}

