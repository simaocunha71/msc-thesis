        String[] valid_endings = {"txt", "exe", "dll"};
        String[] invalid_patterns = {
            ".*\\d{4}.*",
            "^\\d{4}.*",
            ".*\\.\\d.*",
            ".*\\..*\\.$"
        };

        if (file_name.matches(invalid_patterns[0])) {
            return "No";
        }
        if (file_name.matches(invalid_patterns[1])) {
            return "No";
        }
        if (file_name.matches(invalid_patterns[2])) {
            return "No";
        }
        if (file_name.matches(invalid_patterns[3])) {
            return "No";
        }
        String[] parts = file_name.split("\\.");
        if (parts.length != 2) {
            return "No";
        }
        if (parts[0].isEmpty() || !Character.isLetter(parts[0].charAt(0))) {
            return "No";
        }
        for (String ending : valid_endings) {
            if (parts[1].equals(ending)) {
                return "Yes";
            }
        }
        return "No";
    }
}



public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.filenameCheck("example.txt"));
        System.out.println(solution.filenameCheck("1example.dll"));
