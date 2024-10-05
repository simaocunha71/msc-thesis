        int dotIndex = file_name.lastIndexOf('.');
        int countDigit = 0;
        if(dotIndex == -1 || dotIndex == 0 || dotIndex == file_name.length()-1){
            return "No";
        }
        for(int i = 0; i < file_name.length(); i++){
            char ch = file_name.charAt(i);
            if(Character.isDigit(ch)){
                countDigit++;
                if(countDigit > 3){
                    return "No";
                }
            }
        }
        String fileType = file_name.substring(dotIndex+1);
        if(!fileType.equals("txt") && !fileType.equals("exe") && !fileType.equals("dll")){
            return "No";
        }
        char startChar = file_name.charAt(0);
        if(!Character.isLetter(startChar)){
            return "No";
        }
        return "Yes";
    }
}

This is a Java solution to the problem. It checks for the given conditions in the problem statement.

*

*It checks if the file name contains exactly one dot and if it is not at the start or end of the string.

*It counts the number of digits in the file name and returns "No" if more than three digits are present.

*It extracts the substring after the dot and checks if it is one of the allowed extensions: "txt", "exe" or "dll".

*It checks if the first character of the file name is a letter.

If all these conditions are met, it returns "Yes", otherwise "No".
























































































































