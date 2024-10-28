        String vowels = "AEIOUaeiou";
        int i = word.length() - 1;
        while (i >= 0) {
            if (vowels.contains(word.substring(i, i + 1))) {
                return word.substring(i, i + 1);
            }
            i -= 1;
        }
        return "";
    }
}

