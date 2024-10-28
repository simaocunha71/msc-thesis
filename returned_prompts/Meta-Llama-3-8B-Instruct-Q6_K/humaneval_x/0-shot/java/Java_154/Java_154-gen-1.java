public boolean cycpatternCheck(String a, String b) {
    if (a.length() < b.length()) {
        return false;
    }
    for (int i = 0; i < a.length(); i++) {
        a = a.substring(i) + a.substring(0, i);
        if (a.contains(b)) {
            return true;
        }
    }
    return false;
}  //time complexity is O(n^2)  where n is the length of the string a.

