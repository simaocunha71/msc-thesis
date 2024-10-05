        String vowels = "AEIOUaeiou";
        for (int i = word.length() - 2; i > 0; i--) {
            if (vowels.contains(String.valueOf(word.charAt(i))) &&
                    !vowels.contains(String.valueOf(word.charAt(i - 1))) &&
                    !vowels.contains(String.valueOf(word.charAt(i + 1)))) {
                return String.valueOf(word.charAt(i));
            }
        }
        return "";
    }
}

