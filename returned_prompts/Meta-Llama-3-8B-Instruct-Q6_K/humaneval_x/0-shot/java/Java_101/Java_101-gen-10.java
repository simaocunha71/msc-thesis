    public List<String> wordStrings(String s) {
        String[] words = s.split("[,\\s]+");
        List<String> result = new ArrayList<>();
        for (String word : words) {
            result.add(word);
        }
        return result;
    }
}
