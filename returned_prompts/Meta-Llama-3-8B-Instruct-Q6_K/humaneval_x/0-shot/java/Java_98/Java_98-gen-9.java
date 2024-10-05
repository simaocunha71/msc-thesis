    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if ((i % 2 == 0 && Character.isUpperCase(s.charAt(i))) && (Character.isLetter(s.charAt(i)))) {
            count++;
        }
    }
    return count;
}