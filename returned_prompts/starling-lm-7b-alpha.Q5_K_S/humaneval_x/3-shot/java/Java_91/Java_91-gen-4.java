        int result = 0;
        String current_sentence = "";
        for (char c : S.toCharArray()) {
            if (c == '.' || c == '?' || c == '!') {
                if (current_sentence.length() > 0 && current_sentence.charAt(0) == 'I') result += 1;
                current_sentence = "";
            } else {
                current_sentence += c;
            }
        }
        return result;
    }
}

