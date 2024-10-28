        String result = "";
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                result += (char) ((c + 2 * 2 - 'A' + 1) % 26 + 'A');
            } else if (Character.isLowerCase(c)) {
                result += (char) ((c + 2 * 2 - 'a' + 1) % 26 + 'a');
            }
        }
        return result;
    }
}

