        int sum = 0;

        if (lst.size() == 0) return 0;

        int largest = (int) lst.get(0);
        int smallest = (int) lst.get(0);

        for (int i = 0; i < lst.size(); i++) {
            int cur = (int) lst.get(i);

            if (cur > largest) {
                largest = cur;
            }
            if (cur < smallest) {
                smallest = cur;
            }
        }

        for (int i = smallest; i <= largest; i++) {
            if (i % 2 != 0) {
                sum += i * i;
            }
        }
        return sum;
    }
}

