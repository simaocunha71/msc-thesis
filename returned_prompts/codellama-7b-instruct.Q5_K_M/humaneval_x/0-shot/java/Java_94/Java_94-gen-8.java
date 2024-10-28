        for (int i = 0; i < lst.size(); i++) {
            int num = lst.get(i);
            if (num > 1) {
                int count = 0;
                while (num > 0) {
                    if (num % 10 == 0) {
                        break A;
                    }
                    if (num % 10 == 1 || num % 10 == 3 || num % 10 == 7 || num % 10 == 9) {
                        count++;
                    }
                    num = num / 10;
                }
                return count;
            }
            else if (num == 1) {
                return 1;
            }
            else {
                return 0;
            }
        }
        return 0;
    }
}
