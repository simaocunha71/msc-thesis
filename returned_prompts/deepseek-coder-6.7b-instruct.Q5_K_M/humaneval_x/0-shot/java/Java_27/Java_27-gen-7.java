        StringBuilder sb = new StringBuilder(string.length());

        for(char ch : string.toCharArray()) {
            if(Character.isUpperCase(ch)) {
                sb.append(Character.toLowerCase(ch));
            } else if (Character.isLowerCase(ch)) {
                sb.append(Character.toUpperCase(ch));
            } else {
                sb.append(ch);
            }
        }

        return sb.toString();
    }
}


