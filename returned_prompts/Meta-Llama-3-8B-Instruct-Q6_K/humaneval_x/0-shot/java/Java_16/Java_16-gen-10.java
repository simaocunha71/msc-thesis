    int count = 0;
    HashSet<Character> set = new HashSet<>();
    for (char c : string.toLowerCase().toCharArray()) {
        if (!set.contains(c)) {
            set.add(c);
            count++;
        }
    }
    return count;
}
