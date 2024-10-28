    public String filenameCheck(String file_name) {
        String[] extensions = {"txt", "exe", "dll"};
        if (file_name == null || file_name.length() == 0) {
            return "No";
        }
        int dotIndex = file_name.indexOf('.');
        if (dotIndex == -1 || dotIndex == 0 || dotIndex == file_name.length() - 1) {
            return "No";
        }
        String beforeDot = file_name.substring(0, dotIndex);
        String afterDot = file_name.substring(dotIndex + 1);
        if (!beforeDot.matches("[a-zA-Z].*") || !Arrays.asList(extensions).contains(afterDot) || countDigits(beforeDot) > 3) {
            return "No";
        }
        return "Yes";
    }

    private int countDigits(String str) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (Character.isDigit(c)) {
                count++;
            }
        }
        return count;
    }