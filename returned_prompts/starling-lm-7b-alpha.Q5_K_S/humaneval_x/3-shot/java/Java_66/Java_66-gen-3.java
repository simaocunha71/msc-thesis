        int result = 0;
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                result += c;
            }
        }
        return result;
    }
}

