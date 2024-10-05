    public String filenameCheck(String file_name) {
        String[] fileExtensions = {"txt", "exe", "dll"};
        int dotIndex = file_name.indexOf('.');
        if (dotIndex == -1) {
            return "No";
        }
        String beforeDot = file_name.substring(0, dotIndex);
        String afterDot = file_name.substring(dotIndex + 1);
        if (!beforeDot.matches("^[a-zA-Z].*") || beforeDot.matches("\\d+")) {
            return "No";
        }
        if (!Arrays.asList(fileExtensions).contains(afterDot)) {
            return "No";
        }
        int count = (int) beforeDot.chars().filter(c -> Character.isDigit(c)).count();
        if (count > 3) {
            return "No