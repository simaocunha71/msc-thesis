        for  (int i = 2; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i-1) || s.charAt(i-1) == s.charAt(i-2) || s.charAt(i) == s.charAt(i-2))
                return false;
        }
        return s.length() >= 3;
     }
}

