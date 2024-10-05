        String rev = new StringBuilder(string).reverse().toString();
        for(int i = 0; i < rev.length(); i++) {
            if(string.startsWith(rev.substring(i))) {
                return string + rev.substring(i);
            }
        }
        return string + rev;
    }
} 