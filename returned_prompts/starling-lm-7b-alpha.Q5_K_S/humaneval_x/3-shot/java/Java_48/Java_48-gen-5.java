        int length = text.length();
        for (int i = 0; i < length; i++) {
            if (text.charAt(i) != text.charAt(length - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}

