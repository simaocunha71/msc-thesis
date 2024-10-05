        StringBuilder result = new StringBuilder();

        for  (char c : string.toCharArray())  {
            if  (Character.isUpperCase(c))  {
                result.append(Character.toLowerCase(c));
            } else  {
                result.append(Character.toUpperCase(c));
            }
         }

        return result.toString();
     }
}

