        String result = "";
        for(int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if(c >= 'a' && c <= 'z') {
                result += (char) (c - 32);
            } else if(c >= 'A' && c <= 'Z') {
                result += (char) (c + 32);
            } else {
                result += c;
            }
        }
        return result;
    }
}
