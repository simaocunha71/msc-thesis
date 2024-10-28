        int count = 0;
        String lowerCase = s.toLowerCase();

        for(int i = 0; i < lowerCase.length(); i++) {
            char c = lowerCase.charAt(i);
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }

        if(s.charAt(s.length()-1) == 'y') {
            count++;
        }

        return count;
     }
}

