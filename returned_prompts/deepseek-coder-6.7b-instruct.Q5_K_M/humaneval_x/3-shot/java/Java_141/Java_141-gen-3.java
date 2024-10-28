        String[] validExtensions = {"txt", "exe", "dll"};
        List<String> validExtensionsList = Arrays.asList(validExtensions);

        String[] split_name = file_name.split("\\.");

        if (split_name.length != 2) return "No";

        String namePart = split_name[0];
        String extension = split_name[1];

        if (namePart.length() == 0) return "No";
        if (!Character.isLetter(namePart.charAt(0))) return "No";

        int digitCount = 0;
        for (char c : namePart.toCharArray()) {
            if (Character.isDigit(c)) digitCount++;
        }

        if (digitCount > 3) return "No";

        if (!validExtensionsList.contains(extension)) return "No";

        return "Yes";
     }
}

