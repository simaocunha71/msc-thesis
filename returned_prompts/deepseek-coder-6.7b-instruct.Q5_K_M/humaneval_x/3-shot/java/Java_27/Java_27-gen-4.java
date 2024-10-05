        StringBuilder result = new StringBuilder(string.length());
        for(char c : string.toCharArray()) {
            if(Character.isLowerCase(c)) {
                result.append(Character.toUpperCase(c));
            } else if(Character.isUpperCase(c)) {
                result.append(Character.toLowerCase(c));
            }
        }
        return result.toString();
     }
}

