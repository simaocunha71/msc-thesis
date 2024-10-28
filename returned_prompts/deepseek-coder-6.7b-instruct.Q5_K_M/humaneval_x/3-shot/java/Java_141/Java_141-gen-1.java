        int digitCount = 0;
        for  (char c  : file_name.toCharArray()) {
            if  (Character.isDigit(c)) {
                digitCount++;
            }
        }
        if  (digitCount  >  3) return "No";

        int dotIndex = file_name.indexOf('.');
        if  (dotIndex  ==  -1) return "No";

        String baseName = file_name.substring(0, dotIndex);
        String extension = file_name.substring(dotIndex  +  1);

        if  (baseName.isEmpty()  ||  !Character.isLetter(baseName.charAt(0))) return "No";

        if  (!extension.equals("txt")  &&  !extension.equals("exe")  &&  !extension.equals("dll")) return "No";

        return "Yes";
     }
}

