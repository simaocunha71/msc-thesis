        int count = 0;
        for (char c : num.toCharArray()) {
            if (c >= '2' && c <= '7' || c == 'B' || c == 'D') {
                count++;
            }
        }
        return count;
    }
}

