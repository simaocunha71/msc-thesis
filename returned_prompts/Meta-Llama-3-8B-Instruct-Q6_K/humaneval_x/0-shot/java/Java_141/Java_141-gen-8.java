    public String filenameCheck(String file_name) {
        if (file_name == null || file_name.isEmpty()) {
            return "No";
        }

        int dotIndex = file_name.indexOf('.');
        if (dotIndex == -1 || dotIndex == file_name.length() - 1) {
            return "No";
        }

        String beforeDot = file_name.substring(0, dotIndex);
        String afterDot = file_name.substring(dotIndex + 1);

        if (!beforeDot.matches("[a-zA-Z].*") || beforeDot.matches("[0-9]+")) {
            return "No";
        }

        if (beforeDot.isEmpty()) {
            return "No";
        }

        String[] extensions = {"txt", "exe", "dll"};
        if (!Arrays.asList(extensions).contains(afterDot)) {
            return "No";
        }

        int digitCount = (int) beforeDot.chars().filter(Character::isDigit).count();
        if (digitCount > 3) {
            return "No";
        }

        return "Yes";
    }    }
}
