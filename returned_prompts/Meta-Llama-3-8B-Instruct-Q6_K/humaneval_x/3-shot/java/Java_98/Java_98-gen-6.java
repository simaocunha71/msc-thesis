        int count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c) && "AEIOU".indexOf(c) != -1) {
                count++;
            }
        }
        return count;
    }
}

