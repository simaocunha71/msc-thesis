        String vowels = "AEIOUaeiou";
        for (int i = word.length() - 2; i > 0; i--) {
            if (vowels.contains(word.charAt(i) + "") && !vowels.contains(word.charAt(i - 1) + "") && !vowels.contains(word.charAt(i + 1) + "")) {
                return word.charAt(i) + "";
            }
        }
        return "";
    }
}

