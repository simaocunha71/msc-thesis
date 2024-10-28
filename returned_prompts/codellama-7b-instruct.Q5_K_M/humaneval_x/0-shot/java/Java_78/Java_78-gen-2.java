        int count = 0;
        for (int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            switch (c) {
                case 'A':
                case 'B':
                case 'C':
                case 'D':
                case 'E':
                case 'F':
                    count++;
                    break;
            }
        }
        return count;
    }
}

