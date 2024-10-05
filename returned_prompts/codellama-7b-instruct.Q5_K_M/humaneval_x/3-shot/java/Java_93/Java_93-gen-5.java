        String result = "";
        boolean is_vowel = false;
        char current_letter;
        for (int i = 0; i < message.length(); i++) {
            current_letter = message.charAt(i);
            if (current_letter == 'a' || current_letter == 'e' || current_letter == 'i' || current_letter == 'o' || current_letter == 'u') {
                is_vowel = true;
            }

            if (Character.isLetter(current_letter)) {
                if (is_vowel) {
                    if (current_letter < 'z') {
                        result += (char) ((int) current_letter + 2);
                    } else {
                        result += (char) ((int) current_letter - 2);
                    }
                    is_vowel = false;
                } else {
                    if (current_letter < 'Z') {
                        result += (char) (current_letter + 32);
                    } else {
                        result += (char) (current_letter - 32);
                    }
                }
            } else {
                result += current_letter;
            }
        }
        return result;
    }
}

