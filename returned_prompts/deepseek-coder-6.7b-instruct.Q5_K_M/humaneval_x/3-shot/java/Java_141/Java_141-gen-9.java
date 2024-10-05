        String[] validExtensions = {"txt", "exe", "dll"};
        int digitCount = 0;
        int dotCount = 0;

        for (char c : file_name.toCharArray()) {
            if (Character.isDigit(c)) {
                digitCount++;
            }
            if (c == '.') {
                dotCount++;
            }
        }

        if (digitCount > 3 || dotCount != 1) {
            return "No";
        }

        String[] parts = file_name.split("\\.");
        if (!Character.isLetter(parts[0].charAt(0)) || parts[0].length() == 0) {
            return "No";
        }

        if (Arrays.asList(validExtensions).contains(parts[1])) {
            return "Yes";
        }

        return "No";
     }
}

