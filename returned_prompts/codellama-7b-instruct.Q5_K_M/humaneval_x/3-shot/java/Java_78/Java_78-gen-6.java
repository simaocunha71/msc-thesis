        int counter = 0;
        for (int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            if (c == 'A') counter += 10;
            else if (c == 'B') counter += 11;
            else if (c == 'C') counter += 12;
            else if (c == 'D') counter += 13;
            else if (c == 'E') counter += 14;
            else if (c == 'F') counter += 15;
            else counter += (c - '0');
        }
        return counter;
    }
}

