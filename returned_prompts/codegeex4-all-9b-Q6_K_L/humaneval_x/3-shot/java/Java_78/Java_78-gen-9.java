        int count = 0;
        for (char c : num.toCharArray()) {
            switch (c) {
                case '2':
                case '3':
                case '5':
                case '7':
                case 'B':
                case 'D':
                    count += 1;
                    break;
            }
        }
        return count;
    }
}

