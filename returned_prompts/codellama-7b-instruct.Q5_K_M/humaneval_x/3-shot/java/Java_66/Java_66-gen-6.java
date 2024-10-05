        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            if (Character.isUpperCase(current)) {
                result += current;
            }
        }
        return result;
    }
}

