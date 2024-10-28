    int count = 0;
    string = string.toLowerCase();
    Set<Character> set = new HashSet<>();
    for (char c : string.toCharArray()) {
        if (!set.contains(c)) {
            set.add(c);
            count++;
        }
    }
    return count;
}
