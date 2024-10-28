        String[] validExtensions 
            = new String[] { "txt", "exe", "dll" };
        String[] parts 
            = file_name.split("\\.");
        if  (parts.length  != 2)  return "No";
        String namePart 
            = parts[0];
        String extension 
            = parts[1];
        if  (!Character.isLetter(namePart.charAt(0)))  return "No";
        if  (namePart.matches(".*\\d.*"))  {
            int digitsCount 
                = (int)namePart.chars()
                    .filter(Character::isDigit)
                    .count();
            if  (digitsCount  >  3)  return "No";
        }
        for (String validExtension  : validExtensions)  {
            if  (extension.equals(validExtension)) 
                return "Yes";
        }
        return "No";
    }
}

