        for (int i = word.length() - 1; i > 0; i--) {
            char c = word.charAt(i);
            if ("AEIOUaeiou".indexOf(c) != -1) {
                return String.valueOf(c);
            }
        }
        return "";
    }
}

