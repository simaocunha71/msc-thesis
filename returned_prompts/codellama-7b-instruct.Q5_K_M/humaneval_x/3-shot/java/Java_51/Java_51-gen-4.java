        String vowels = "aeiouAEIOU";
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            if (!vowels.contains(String.valueOf(text.charAt(i)))) {
                result += text.charAt(i);
            }
        }
        return result;
    }
}

