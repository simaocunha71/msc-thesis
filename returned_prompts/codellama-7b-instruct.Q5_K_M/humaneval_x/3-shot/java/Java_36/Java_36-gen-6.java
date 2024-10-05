        int result = 0;

        for (int i = 0; i < n; i++) {
            if ((i % 11 == 0) || (i % 13 == 0)) {
                String number = String.valueOf(i);
                for (char c : number.toCharArray()) {
                    if (c == '7') {
                        result += 1;
                    }
                }
            }
        }
        return result;
    }
}

