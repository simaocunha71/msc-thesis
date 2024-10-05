        String vowels = "AEIOUaeiou";
        for (int i = 0; i < word.length(); i++) {
            if (vowels.indexOf(word.charAt(i)) >= 0) {
                if (i > 0 && !vowels.contains(word.charAt(i - 1) + "")) return word.charAt(i) + "";
                if (i < word.length() - 1 && !vowels.contains(word.charAt(i + 1) + "")) return word.charAt(i) + "";
                return "";
            }
        }
        return "";
    }
}

