        int len = txt.length();
        boolean result = false;
        if (len > 0) {
            char last_char = txt.charAt(len - 1);
            if (Character.isLetter(last_char)) result = true;
        }
        return result;
    }
}

