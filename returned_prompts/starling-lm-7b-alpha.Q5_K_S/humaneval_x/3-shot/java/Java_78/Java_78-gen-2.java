        int result = 0;
        for (char c : num.toCharArray()) {
            if (c >= '0' && c <= '9') {
                if (c == '9') result += 1;
                else if (c == '8') result += 2;
                else if (c == '7') result += 3;
                else if (c == '6') result += 4;
                else if (c == '5') result += 5;
                else if (c == '4') result += 6;
                else if (c == '3') result += 7;
                else if (c == '2') result += 8;
                else if (c == '1') result += 9;
            } else if (c >= 'A' && c <= 'F') {
                if (c == 'F') result += 1;
                else if (c == 'E') result += 2;
                else if (c == 'D') result += 3;
                else if (c == 'C') result += 4;
                else if (c == 'B') result += 5;
                else if (c == 'A') result += 6;
            }
        }
        return result;
    }
}

