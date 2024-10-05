        int upper = 0;
        for (int i = 0; i < value.length(); i++) {
            if (Character.isUpperCase(value.charAt(i))) upper++;
        }
        return upper;
    }

    public int countLower(String value) {
        int lower = 0;
        for (int i = 0; i < value.length(); i++) {
            if (Character.isLowerCase(value.charAt(i))) lower++;
        }
        return lower;
    }
}

