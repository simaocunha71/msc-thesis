        int length = text.length();
        for (int i = 0; i < length/2; i++) {
            if (text.charAt(i) != text.charAt(length-i-1)) {
                return false;
            }
        }
        return true;
    }
}

