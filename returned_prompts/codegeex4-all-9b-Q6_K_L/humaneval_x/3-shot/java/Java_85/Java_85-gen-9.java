        int sum = 0;
        for (int i = 1; i < lst.size(); i += 2) {
            int val = lst.get(i);
            if (val % 2 == 0) sum += val;
        }
        return sum;
    }
}

