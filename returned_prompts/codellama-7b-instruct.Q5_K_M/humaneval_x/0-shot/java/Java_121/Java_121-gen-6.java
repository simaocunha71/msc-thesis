        int sum = 0;

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) % 2 == 0) {
                continue A;
            }
            sum += lst.get(i);
        }
        return sum;
    }
}

