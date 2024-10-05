        String vowels = "AEIOU";
        int index = word.length() - 1;
        while (index > 0 && vowels.indexOf(word.charAt(index)) == -1) {
            index -= 1;
        }
        if (index <= 0) return "";
        if (vowels.indexOf(word.charAt(index - 1)) != -1) return "";
        return word.charAt(index) + "";
    }
}

