        int index = word.length() - 1;
        while (index >= 0) {
            char c = word.charAt(index);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                if (index < word.length() - 2 && word.charAt(index + 1) == ' ') {
                    return "" + c;
                } else if (index < word.length() - 1 && word.charAt(index + 1) != ' ') {
                    index -= 1;
                } else {
                    return "" + c;
                }
            }
            index -= 1;
        }
        return "";
    }
}

