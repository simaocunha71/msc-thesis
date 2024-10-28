        int result = 0;
        for (int i = 0; i < s.length(); i+=2) {
            if (s.charAt(i) == 'A' || s.charAt(i) == 'E' || s.charAt(i) == 'O' || s.charAt(i) == 'U' || s.charAt(i) == 'I') result += 1;
        }
        return result;
    }
}

