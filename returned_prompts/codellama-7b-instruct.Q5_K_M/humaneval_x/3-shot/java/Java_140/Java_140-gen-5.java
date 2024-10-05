        String result = "";
        char[] text_array = text.toCharArray();
        for (int i = 0; i < text_array.length; i++) {
            if (text_array[i] == ' ') {
                if (i == 0 || text_array[i - 1] != ' ') {
                    result += '_';
                } else {
                    result += '-';
                }
            } else {
                result += text_array[i];
            }
        }
        return result;
    }
}

