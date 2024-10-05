        int i = 0;
        int j = 0;
        int len = word.length();
        while (i < len && j < len) {
            if (Character.isLetter(word.charAt(i)) && !Character.isDigit(word.charAt(i))) {
                j = i + 1;
                while (j < len && Character.isLetter(word.charAt(j))) {
                    j++;
                }
                if (!Character.isDigit(word.charAt(j))) {
                    return String.valueOf(word.charAt(j));
                } else {
                    j++;
                }
            } else {
                i++;
            }
        }
        return "";
    }
}

