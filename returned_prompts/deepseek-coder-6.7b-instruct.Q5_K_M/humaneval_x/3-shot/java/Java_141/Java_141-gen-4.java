        String[] parts = file_name.split("\\.");
        if  (parts.length  != 2)  return "No";

        String name  part[0];
        String extension  part[1];

        if  (name.length()  != 0  && name.matches(".*[0-9]{4,}.*"))  return "No";
        if  (!name.matches("[a-zA-Z].*"))  return "No";

        if  (extension.equals("txt")  ||  extension.equals("exe")  ||  extension.equals("dll"))  {
            return "Yes";
         } else  {
            return "No";
         }
      }
}

