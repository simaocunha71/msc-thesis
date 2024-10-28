        int result = 0;

        for (char c : num.toCharArray()) {
            int value = Character.digit(c, 16);
            if (value == 2 || value == 3 || value == 5 || value == 7 || value == 11 || value == 13) {
                result += 1;
            }
        }

        return result;
    }
}

