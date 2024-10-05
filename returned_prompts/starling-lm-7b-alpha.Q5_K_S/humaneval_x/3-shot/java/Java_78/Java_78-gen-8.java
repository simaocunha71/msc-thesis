        int result = 0;
        for (int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            if (c == '0') result += 0;
            else if (c == '1') result += 1;
            else if (c == '2') result += 2;
            else if (c == '3') result += 3;
            else if (c == '4') result += 4;
            else if (c == '5') result += 5;
            else if (c == '6') result += 6;
            else if (c == '7') result += 7;
            else if (c == '8') result += 8;
            else if (c == '9') result += 9;
            else if (c == 'A') result += 10;
            else if (c == 'B') result += 11;
            else if (c == 'C') result += 12;
            else if (c == 'D') result += 13;
            else if (c == 'E') result += 14;
            else if (c == 'F') result += 15;
        }
        return result;
    }
}

