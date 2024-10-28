        int result = 0;

        for (int i = 0; i < num.length(); i++) {
            char hex = num.charAt(i);

            switch (hex) {
                case 'A':
                case 'B':
                case 'C':
                case 'D':
                case 'E':
                case 'F':
                    result++;
                    break;
            }
        }

        return result;
    }
}

