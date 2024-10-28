        int sum = 0;
        int max = 0;
        int min = 0;

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) instanceof Integer) {
                int n = (int) lst.get(i);
                if (n > max) max = n;
                if (n < min) min = n;
            }
        }

        for (int i = min; i < max; i++) {
            sum += i * i;
        }
        return sum;
    }
}

