        int count = 0;

        for (int i = 0; i < num.length(); i++) {
            char ch = num.charAt(i);

            if (ch == '2' || ch == '3' || ch == '5' || ch == '7' ||
                ch == 'B' || ch == 'D' || ch == '9' || ch == 'A' ||
                ch == 'C' || ch == 'E' || ch == 'F') {
                if (checkPrime(ch))
                    count++;
            }
        }

        return count;
    }

    public boolean checkPrime(char ch) {
        int number = 0;
        if (ch == '2' || ch == '3' || ch == '5' || ch == '7' ||
            ch == 'B' || ch == 'D' || ch == '9' || ch == 'A' ||
            ch == 'C' || ch == 'E' || ch == 'F') {
            if (ch == '2')
                number = 2;
            else if (ch == '3')
                number = 3;
            else if (ch == '5')
                number = 5;
            else if (ch == '7')
                number = 7;
            else if (ch == 'B')
                number = 11;
            else if (ch == 'D')
                number = 13;
            else if (ch == '9')
                number = 9;
            else if (ch == 'A')
                number = 10;
            else if (ch == 'C')
                number = 12;
            else if (ch == 'E')
                number = 14;
            else if (ch == 'F')
                number = 15;

            for (int i = 2; i < number; i++) {
                if (number % i == 0)
                    return false;
            }
            return true;
        } else
            return false;
    }
}








