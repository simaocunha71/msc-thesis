        int right = 0;
        int left = word.length() - 1;
        while (right < left) {
            if (isVowel(word.charAt(right))) {
                return String.valueOf(word.charAt(right));
            }
            if (isVowel(word.charAt(left))) {
                return String.valueOf(word.charAt(left));
            }
            right++;
            left--;
        }
        return "";
    }

    private boolean isVowel(char ch) {
        return "aeiouAEIOU".indexOf(ch) != -1;
    }
}












