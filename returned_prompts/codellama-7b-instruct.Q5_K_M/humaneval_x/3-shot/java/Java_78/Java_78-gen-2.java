        int count = 0;
        for (int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            if (c == 'A') count++;
            else if (c == 'B') count++;
            else if (c == 'C') count++;
            else if (c == 'D') count++;
            else if (c == 'E') count++;
            else if (c == 'F') count++;
        }
        return count;
    }
}

