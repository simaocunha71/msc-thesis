        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        return sum <= w && new String(q).equals(new String(q).reverse());
    }
}

