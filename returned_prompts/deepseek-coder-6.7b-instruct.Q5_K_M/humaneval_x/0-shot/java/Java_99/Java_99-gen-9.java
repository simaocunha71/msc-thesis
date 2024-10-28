    int count = 0;
    String[] split = value.split("\\.");
    String str = split[0];
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (Character.isDigit(c)) {
            count++;
        }
    }
    return count;
}

public int countLower(String value)  {

    int count = 0;
    String[] split = value.split("\\.");
    String str = split[0];
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (Character.isLowerCase(c)) {
            count++;
        }
    }
    return count;
}

public int countSpecial(String value)  {

    int count = 0;
    String[] split = value.split("\\.");
    String str = split[0];
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (!Character.isLetterOrDigit(c) && c != ' ') {
            count++;
        }
    }
    return count;
}

public int countDigits(String value)  {

    int count = 0;
    String[] split = value.split("\\.");
    String str = split[0];
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (Character.isDigit(c)) {
            count++;
        }
    }
    return count;
}

public int countLetters(String value)  {

    int count = 0;
    String[] split = value.split("\\.");
    String str = split[0];
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (Character.isLetter(c)) {
            count++;
        }
    }
    return count;
