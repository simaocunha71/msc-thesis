    int count = 0;
    for (int i = 0; i < string.length(); i++) {
        char c = Character.toLowerCase(string.charAt(i));
        boolean found = false;
        for (int j = 0; j < i; j++) {
            if (c == Character.toLowerCase(string.charAt(j))) {
                found = true;
                break;
            }
        }
        if (!found) {
            count++;
        }
    }
    return count;
}
