public Optional<String> longest(List<String> strings) {
    if(strings == null || strings.isEmpty()) {
        return Optional.empty();
    }
    String longest = strings.get(0);
    for(String s : strings) {
        if(s.length() > longest.length()) {
            longest = s;
        }
    }
    return Optional.of(longest);
}