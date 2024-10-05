        int count = 0;
        for (int i = 0; i < num.length(); i++) {
            if (num.charAt(i) == 'A' || num.charAt(i) == 'B' || num.charAt(i) == 'D' || num.charAt(i) == 'E' || num.charAt(i) == 'F') {
                count++;
            }
        }
        return count;
    }
}






