        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (!isVowel(c)) result.append(c);
        }
        return result.toString();
    }

    private boolean isVowel(char c) {
        String vowels = "aeiouAEIOU";
        return vowels.indexOf(c) != -1;
    }
}

