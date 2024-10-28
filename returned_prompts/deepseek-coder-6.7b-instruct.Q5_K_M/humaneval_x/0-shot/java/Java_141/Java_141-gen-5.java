        String[] arr = file_name.split("\\.");

        if (arr.length != 2) {
            return "No";
        }

        if (!Character.isLetter(arr[0].charAt(0))) {
            return "No";
        }

        String digits = "0123456789";
        int count = 0;
        for (char c : arr[0].toCharArray()) {
            if (digits.contains(Character.toString(c))) {
                count++;
            }
        }

        if (count > 3) {
            return "No";
        }

        String[] validExtensions = {"txt", "exe", "dll"};
        if (!Arrays.asList(validExtensions).contains(arr[1])) {
            return "No";
        }

        return "Yes";
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.filenameCheck("example.txt")); //  "Yes"
        System.out.println(solution.filenameCheck("1example.dll")); //  "No"
    }
}
























































































































































































































