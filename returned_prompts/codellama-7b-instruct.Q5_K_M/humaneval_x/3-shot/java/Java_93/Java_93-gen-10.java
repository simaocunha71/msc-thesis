        String result = "";
        int current_index = 0;

        while (current_index < message.length()) {
            char current_char = message.charAt(current_index);
            if (current_char >= 'a' && current_char <= 'z') {
                if (current_char == 'a' || current_char == 'e' || current_char == 'i' || current_char == 'o' || current_char == 'u') {
                    result += (char) ((current_char - 'a' + 2 + 'A') % 26 + 'A');
                } else {
                    result += (char) ((current_char - 'a' + 'A') % 26 + 'A');
                }
            } else if (current_char >= 'A' && current_char <= 'Z') {
                if (current_char == 'A' || current_char == 'E' || current_char == 'I' || current_char == 'O' || current_char == 'U') {
                    result += (char) ((current_char - 'A' + 2 + 'a') % 26 + 'a');
                } else {
                    result += (char) ((current_char - 'A' + 'a') % 26 + 'a');
                }
            } else {
                result += current_char;
            }

            current_index += 1;
        }
        return result;
    }
}

