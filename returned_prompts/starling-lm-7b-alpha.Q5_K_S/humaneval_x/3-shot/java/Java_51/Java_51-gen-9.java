        String vowels = "aeiouAEIOU";
        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (!vowels.contains(String.valueOf(c))) {
                result.append(c);
            }
        }
        return result.toString();
    }
}

