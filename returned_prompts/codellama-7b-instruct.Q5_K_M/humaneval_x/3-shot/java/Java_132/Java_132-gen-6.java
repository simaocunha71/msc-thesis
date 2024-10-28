        if (string.length() == 0) return false;
        if (string.length() == 1) return false;
        if (string.length() == 2) return false;
        if (string.length() == 3) return false;
        if (string.length() == 4) return false;
        if (string.length() == 5) return false;
        if (string.length() == 6) return false;

        int left_brackets = 0;
        int right_brackets = 0;

        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == '[') left_brackets += 1;
            if (string.charAt(i) == ']') right_brackets += 1;
        }

        if (left_brackets == right_brackets) return false;

        return true;

    }
}

