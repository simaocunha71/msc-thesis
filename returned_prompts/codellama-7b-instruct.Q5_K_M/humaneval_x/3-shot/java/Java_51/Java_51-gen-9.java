        String vowels = "aeiouAEIOU";
        StringBuilder sb = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (!vowels.contains(Character.toString(c))) {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}

