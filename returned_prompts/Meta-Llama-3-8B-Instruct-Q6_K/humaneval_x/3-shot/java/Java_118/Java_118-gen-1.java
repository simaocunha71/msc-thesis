        String vowels = "aeiouAEIOU";
        StringBuilder result = new StringBuilder();
        for (int i = word.length() - 1; i >= 0; i--) {
            if (!vowels.contains(String.valueOf(word.charAt(i)))) {
                for (int j = i - 1; j >= 0; j--) {
                    if (vowels.contains(String.valueOf(word.charAt(j)))) {
                        result.append(word.charAt(j));
                        break;
                    }
                }
                if (result.length() == 0) {
                    result.append("");
                }
                break;
            }
        }
        return result.toString();
    }
}

