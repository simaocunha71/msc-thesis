        int result = 0;
        for (int i = 0; i < value.length(); i++) {
            if (Character.isUpperCase(value.charAt(i))) {
                result += 1;
            }
        }
        return result;
    }
}

