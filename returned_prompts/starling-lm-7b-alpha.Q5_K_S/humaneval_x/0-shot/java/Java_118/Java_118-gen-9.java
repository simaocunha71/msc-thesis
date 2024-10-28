        String vowels = "aeiouAEIOU";
        int len = word.length();
        int index1 = -1;
        int index2 = -1;
        for (int i = 1; i < len - 1; i++) {
            if (vowels.contains(String.valueOf(word.charAt(i)))) {
                if (index1 == -1) {
                    index1 = i;
                } else {
                    index2 = i;
                }
            }
        }
        if (index1 == -1 && index2 == -1) {
            return "";
        }
        int left = index1;
        int right = index2;
        if (left == -1 || right == -1 || left >= right) {
            return String.valueOf(word.charAt(left));
        }
        int min = Math.min(left, right);
        int max = Math.max(left, right);
        int diff1 = min - 1;
        int diff2 = max + 1;
        if (diff1 < 0 || diff2 >= len) {
            if (left == min) {
                return String.valueOf(word.charAt(left));
            } else {
                return String.valueOf(word.charAt(max));
            }
        }
        char minChar = word.charAt(diff1);
        char maxChar = word.charAt(diff2);
        if (vowels.contains(String.valueOf(minChar)) && vowels.contains(String.valueOf(maxChar))) {
            if (String.valueOf(minChar).compareTo(String.valueOf(maxChar)) < 0) {
                return String.valueOf(minChar);
            } else {
                return String.valueOf(maxChar);
            }
        } else if (vowels.contains(String.valueOf(minChar))) {
            return String.valueOf(minChar);
        } else if (vowels.contains(String.valueOf(maxChar))) {
            return String.valueOf(maxChar);
        } else {
            return "";
        }
    }
}

