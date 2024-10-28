        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            int value = lst.get(i);
            if (i % 3 == 0) value = value * value;
            if (i % 4 == 0) value = value * value * value;
            sum += value;
        }
        return sum;
    }
}

