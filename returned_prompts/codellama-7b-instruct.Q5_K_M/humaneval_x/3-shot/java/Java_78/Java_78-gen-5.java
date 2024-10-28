        int result = 0;

        for (int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            if (c == 'A') result += 10;
            else if (c == 'B') result += 11;
            else if (c == 'C') result += 12;
            else if (c == 'D') result += 13;
            else if (c == 'E') result += 14;
            else if (c == 'F') result += 15;
            else result += Character.getNumericValue(c);
        }

        return Integer.bitCount(result);
    }
}

