        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if(Character.isLowerCase(c)) {
                sb.append(Character.toUpperCase(c));
            } else {
                sb.append(Character.toLowerCase(c));
            }
        }
        return sb.toString();
    }
}
