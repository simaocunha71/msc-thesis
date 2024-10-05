        int result = 0;
        for (int i = 0; i < num.length(); i++) {
            switch (num.charAt(i)) {
                case '0':
                case '1':
                case '2':
                case '3':
                case '4':
                case '5':
                case '6':
                case '7':
                case '8':
                case '9':
                    result++;
                    break;
                case 'A':
                case 'B':
                case 'C':
                case 'D':
                case 'E':
                case 'F':
                    result += 2;
                    break;
                default:
                    break;
            }
        }
        return result;
    }
}

