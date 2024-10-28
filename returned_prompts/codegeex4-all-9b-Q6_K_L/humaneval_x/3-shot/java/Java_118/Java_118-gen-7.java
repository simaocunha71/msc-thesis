        String vowels = "AEIOUaeiou";
        for (int i = word.length() - 1; i >= 1; i--) {
            if (vowels.contains(word.substring(i - 1, i + 1))) {
                return word.substring(i, i + 1);
            }
        }
        return "";
    }
}

