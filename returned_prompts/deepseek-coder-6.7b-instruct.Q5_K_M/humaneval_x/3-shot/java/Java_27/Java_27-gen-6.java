        StringBuilder sb = new StringBuilder(string.length());

        for(char c : string.toCharArray()) {
            if (Character.isUpperCase(c)) {
                sb.append(Character.toLowerCase(c));
            } else if (Character.isLowerCase(c)) {
                sb.append(Character.toUpperCase(c));
            }
        }

        return sb.toString();
     }
}

