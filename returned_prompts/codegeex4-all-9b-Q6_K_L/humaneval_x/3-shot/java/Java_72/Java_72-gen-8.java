        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        return sum <= w && q.equals(new ArrayList<Integer>(q).reverse());
    }
}

