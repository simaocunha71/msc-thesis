        int count = 0;
        String vowels = "aeiou";
        String y = "y";

        for  (int i = 0; i < s.length(); i++) {
            if  (vowels.contains(Character.toString(s.charAt(i)).toLowerCase())) {
                count++;
            }
            if  (i == s.length() - 1 && y.contains(Character.toString(s.charAt(i)).toLowerCase())) {
                count++;
            }
        }
        return count;
     }
}

