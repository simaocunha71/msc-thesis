        String[] validExtensions = {"txt", "exe", "dll"};
        int digitCount = 0;

        for(char c : file_name.toCharArray()) {
            if(Character.isDigit(c)) {
                digitCount++;
            }
        }

        if(digitCount > 3 || !file_name.contains(".")) {
            return "No";
        }

        String[] split_name = file_name.split("\\.");
        if(split_name[0].isEmpty() || !Character.isLetter(split_name[0].charAt(0)) || !Arrays.asList(validExtensions).contains(split_name[1])) {
            return "No";
        }

        return "Yes";
     }
}

