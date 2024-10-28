    int len = value.length();
    int index = 0;
    int upper = 0;
    for (index = 0; index < len; index++) {
        if (value.charAt(index) >= 'A' && value.charAt(index) <= 'Z') {
            upper++;
        }
    }

    return upper;
}

    public int countLower(String value) {
        int len = value.length();
        int index = 0;
        int lower = 0;
        for (index = 0; index < len; index++) {
            if (value.charAt(index) >= 'a' && value.charAt(index) <= 'z') {
                lower++;
            }
        }

        return lower;
    }

    public int countDigit(String value) {
        int len = value.length();
        int index = 0;
        int digit = 0;
        for (index = 0; index < len; index++) {
            if (value.charAt(index) >= '0' && value.charAt(index) <= '9') {
                digit++;
            }
        }

        return digit;
    }

    public int countSpecialChar(String value) {
        int len = value.length();
        int index = 0;
        int specialChar = 0;
        for (index = 0; index < len; index++) {
            if (!(value.charAt(index) >= '0' && value.charAt(index) <= '9') && !(value.charAt(index) >= 'A' && value.charAt(index) <= 'Z') && !(value.charAt(index) >= 'a' && value.charAt(index) <= 'z')) {
                specialChar++;
            }
        }

        return specialChar;
    }

    public int countLetters(String value) {
        int len = value.length();
        int index = 0;
        int letter = 0;
        for (index = 0; index < len; index++) {
            if (value.charAt(index) >= 'A