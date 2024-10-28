        String[] validExtensions = {"txt", "exe", "dll"};

        int dotIndex = file_name.lastIndexOf('.');
        if(dotIndex == -1 || dotIndex == 0 || dotIndex == file_name.length() - 1) {
            return "No";
        }

        String name = file_name.substring(0, dotIndex);
        String extension = file_name.substring(dotIndex + 1);

        if(!Character.isLetter(name.charAt(0)) || name.matches(".*\\d{4,}.*")) {
            return "No";
        }

        int digitCount = 0;
        for(char c : name.toCharArray()) {
            if(Character.isDigit(c)) {
                digitCount++;
                if(digitCount > 3) {
                    return "No";
                }
            }
        }

        for(String ext : validExtensions) {
            if(ext.equals(extension)) {
                return "Yes";
            }
        }

        return "No";
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.filenameCheck("example.txt")); // Yes
        System.out.println(sol.filenameCheck("1example.dll")); // No
        System.out.println(sol.filenameCheck("example1.dll")); // Yes
        System.out.println(sol.filenameCheck("example.java")); // No
        System.out.println(sol.filenameCheck(".txt")); // No
        System.out.println(sol.filenameCheck("example")); // No
        System.out.println(sol.filenameCheck("e1xample2.txt")); // Yes
        System.out.println(sol.filenameCheck("e1xample2222.txt")); // No
    }
}

This program checks if the filename is valid by checking if it contains a single dot, if the name starts with a letter, if there are no more than three digits, and if the extension is one of the valid extensions ("txt",