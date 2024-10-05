        String vowels = "AEIOUaeiou";
        for (int i = word.length() - 2; i > 0; i--) {
            char c = word.charAt(i);
            if (vowels.contains(String.valueOf(c))) {
                return String.valueOf(c);
            }
        }
        return "";
    }
}

