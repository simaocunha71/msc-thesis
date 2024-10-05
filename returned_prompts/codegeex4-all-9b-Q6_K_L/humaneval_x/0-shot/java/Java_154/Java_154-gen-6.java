public boolean cycpatternCheck(String a, String b) {
    Set<String> set = new HashSet<>();
    for (int i = 0; i < b.length(); i++) {
        set.add(b.substring(i) + b.substring(0, i));
    }
    return a.contains(b) || set.stream().anyMatch(a::contains);
}