        int count = 0;
        for (int i = 11; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String number = String.valueOf(i);
                for (int j = 0; j < number.length(); j++) {
                    if (number.charAt(j) == '7') {
                        count++;
                        break;
                    }
                }
            }
        }
        return count;
    }
}

