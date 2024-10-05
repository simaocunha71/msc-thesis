        int result = 0;
        for (char c : s.toCharArray()) {
            switch (c) {
                case 'a':
                case 'e':
                case 'i':
                case 'o':
                case 'u':
                case 'A':
                case 'E':
                case 'I':
                case 'O':
                case 'U':
                case 'y':
                case 'Y':
                    result += 1;
                    break;
            }
        }
        return result;
    }
}

