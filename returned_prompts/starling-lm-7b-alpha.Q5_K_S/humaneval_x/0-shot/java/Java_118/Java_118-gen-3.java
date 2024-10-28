    int len = word.length();
    int first = 0;
    int second = 0;
    char vowel = ' ';
    boolean found = false;

    for(int i = 0; i < len; i++) {
        char c = word.charAt(i);
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            first = i;
            found = true;
            break;
        }
    }

    if(!found) {
        return "";
    }

    found = false;
    for(int i = len - 1; i >= 0; i--) {
        char c = word.charAt(i);
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            second = i;
            found = true;
            break;
        }
    }

    if(!found) {
        return "";
    }

    int diff = second - first;
    int diff1 = Math.min(diff, len - diff);
    int diff2 = Math.max(diff, len - diff);

    if(diff1 == diff2) {
        return word.charAt(first);
    }

    if(diff1 < diff2) {
        return word.charAt(first);
    }

    return word.charAt(second);
}
}
























































































































































