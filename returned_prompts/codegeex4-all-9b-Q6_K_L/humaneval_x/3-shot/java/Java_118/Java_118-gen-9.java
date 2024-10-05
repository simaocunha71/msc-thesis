        String vowels = "AEIOUaeiou";
        int index = word.length() - 1;
        while (index > 0) {
            if (vowels.contains(String.valueOf(word.charAt(index)))) {
                return String.valueOf(word.charAt(index));
            }
            index -= 1;
        }
        return "";
    }
}

