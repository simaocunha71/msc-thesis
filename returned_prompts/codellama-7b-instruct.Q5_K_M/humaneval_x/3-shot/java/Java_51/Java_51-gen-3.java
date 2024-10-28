        String vowels = "aeiouAEIOU";
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            if (vowels.indexOf(text.charAt(i)) == -1) {
                result.append(text.charAt(i));
            }
        }
        return result.toString();
    }
}

