        int count = 0;
        for (int i = 0; i < num.length(); i++) {
            char current = num.charAt(i);
            switch (current) {
                case 'A':
                case 'B':
                case 'C':
                case 'D':
                case 'E':
                case 'F':
                    count++;
                    break A;
                default:
                    break;
            }
        }
        return count;
    }
}


