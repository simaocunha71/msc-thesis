    public String filenameCheck(String file_name) {
        String[] extensions = {"txt", "exe", "dll"};
        String[] parts = file_name.split("\\.");
        if (parts.length != 2) {
            return "No";
        }
        if (!isLatinLetter(parts[0].charAt(0))) {
            return "No";
        }
        if (parts[0].matches("[0-9]+")) {
            return "No";
        }
        if (parts[0].length() > 1 && parts[0].matches("[0-9]+")) {
            return "No";
        }
        if (!Arrays.asList(extensions).contains(parts[1])) {
            return "No";
        }
        return "Yes";
    }
    
    private boolean isLatinLetter(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }
}
