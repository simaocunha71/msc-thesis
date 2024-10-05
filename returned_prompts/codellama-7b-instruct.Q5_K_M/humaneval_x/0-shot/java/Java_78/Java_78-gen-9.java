        int count = 0;
        String hex = "0123456789ABCDEF";
        for(int i = 0; i < num.length(); i++) {
            for(int j = 0; j < hex.length(); j++) {
                if(num.charAt(i) == hex.charAt(j)) {
                    count++;
                }
            }
        }
        return count;
    }
}

