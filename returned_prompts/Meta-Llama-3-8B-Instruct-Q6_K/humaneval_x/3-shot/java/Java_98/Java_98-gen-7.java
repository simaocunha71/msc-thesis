        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0 && "AEIOU".indexOf(s.charAt(i)) != -1) {
                count++;
            }
        }
        return count;
    }
}

