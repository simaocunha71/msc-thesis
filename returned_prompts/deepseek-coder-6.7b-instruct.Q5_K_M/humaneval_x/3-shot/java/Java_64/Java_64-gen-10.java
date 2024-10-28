        int count = 0;
        String lower_s = s.toLowerCase();

        for  (int i = 0; i < lower_s.length(); i++) {
            char c = lower_s.charAt(i);
            if  (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }

        if  (s.charAt(s.length() - 1) == 'y') {
            count++;
        }

        return count;
     }
}

