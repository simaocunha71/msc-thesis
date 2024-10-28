        String result = "";
        boolean consecutive_spaces = false;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (consecutive_spaces) result += "-";
                else {
                    result += "_";
                    consecutive_spaces = true;
                }
            } else {
                result += c;
                consecutive_spaces = false;
            }
        }
        return result;
    }
}

