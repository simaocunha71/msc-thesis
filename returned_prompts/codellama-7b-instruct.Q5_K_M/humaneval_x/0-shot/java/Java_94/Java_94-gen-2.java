        int max = 0;
        for (int i = 0; i < lst.size(); i++) {
            int temp = lst.get(i);
            if (temp > max) {
                max = temp;
            }
        }

        int sum = 0;
        while (max > 0) {
            sum += max % 10;
            max /= 10;
        }

        return sum;
    }
}
