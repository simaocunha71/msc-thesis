        int count = 0;
        for  (int i = 0; i < s.length(); i += 2) {
            if  (Character.isUpperCase(s.charAt(i)) && "AEIOU".contains(Character.toString(s.charAt(i)))) {
                count++;
            }
        }
        return count;
    }
}

