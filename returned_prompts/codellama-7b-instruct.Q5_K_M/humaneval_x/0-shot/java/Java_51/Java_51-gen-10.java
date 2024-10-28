        String output = "";
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < text.length(); i++) {
            if (vowels.indexOf(text.charAt(i)) == -1) {
                output += text.charAt(i);
            }
        }
        return output;
    }
}
