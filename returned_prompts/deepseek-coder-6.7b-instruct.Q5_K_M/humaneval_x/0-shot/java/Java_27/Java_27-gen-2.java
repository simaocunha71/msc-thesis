        StringBuilder sb = new StringBuilder(string.length());

        for(char ch: string.toCharArray()) {
            if(Character.isUpperCase(ch)) {
                sb.append(Character.toLowerCase(ch));
            } else {
                sb.append(Character.toUpperCase(ch));
            }
        }

        return sb.toString();
    }
}

