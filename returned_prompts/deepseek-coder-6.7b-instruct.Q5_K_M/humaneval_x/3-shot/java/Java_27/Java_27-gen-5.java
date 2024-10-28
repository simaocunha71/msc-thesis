        StringBuilder result = new StringBuilder();

        for  (char c : string.toCharArray()) {
            if  (Character.isLowerCase(c)) {
                result.append(Character.toUpperCase(c));
            } else {
                result.append(Character.toLowerCase(c));
            }
        }

        return result.toString();
     }
}

