        StringBuilder result = new StringBuilder();
        for(char c : s.toCharArray()){
            if(Character.isLetter(c)){
                if(Character.isLowerCase(c))
                    result.append(Character.toUpperCase(c));
                else
                    result.append(Character.toLowerCase(c));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

