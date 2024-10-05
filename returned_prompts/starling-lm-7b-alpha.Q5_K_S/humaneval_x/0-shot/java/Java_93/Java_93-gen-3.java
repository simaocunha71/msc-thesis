    StringBuilder sb = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (c >= 'a' && c <= 'z') {
            sb.append((char) (c - 'a' + 'A'));
        } else if (c >= 'A' && c <= 'Z') {
            sb.append((char) (c - 'A' + 'a'));
        } else if (c == ' ' || c == '.') {
            sb.append(c);
        } else {
            sb.append(c);
        }
    }
    String result = sb.toString();

    StringBuilder sb2 = new StringBuilder();
    for (char c : result.toCharArray()) {
        if (c == ' ') {
            sb2.append(c);
        } else if (c == '.') {
            sb2.append(c);
        } else {
            sb2.append((char) (c - 32));
        }
    }
    result = sb2.toString();

    StringBuilder sb3 = new StringBuilder();
    for (char c : result.toCharArray()) {
        if (c == ' ') {
            sb3.append(c);
        } else if (c == '.') {
            sb3.append(c);
        } else {
            if (c == 'Q') {
                sb3.append('E');
            } else if (c == 'W') {
                sb3.append('R');
            } else if (c == 'E') {
                sb3.append('W');
            } else if (c == 'R') {
                sb3.append('Q');
            } else if (c == 'A') {
                sb3.append('S');
            } else if (c == 'S') {
                sb3.append('A');
            } else if (c == 'I') {
                sb3.append('O');
            } else if (c == 'O') {
                sb3.append('I');
            } else if (c == 'U') {
                sb3.append('P');
            } else if (c ==