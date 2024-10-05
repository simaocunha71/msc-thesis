        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ("AEIOUaeiou".indexOf(c) != -1) {
                count++;
            }
        }
        if (s.charAt(s.length() - 1) == 'y' || s.charAt(s.length() - 1) == 'Y') {
            count++;
        }
        return count;
     }
}

