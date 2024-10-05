        int sum = 0;

        for (int i = 0; i < lst.size(); i++) {
            int current = lst.get(i);

            if (i % 3 == 0) {
                current = current * current;
            } else if (i % 4 == 0 && i % 3 != 0) {
                current = current * current * current;
            }

            sum += current;
        }
        return sum;
    }
}

