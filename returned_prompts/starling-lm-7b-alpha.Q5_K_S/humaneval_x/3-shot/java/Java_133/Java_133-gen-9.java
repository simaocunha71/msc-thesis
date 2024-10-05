        List<Integer> rounded_lst = new ArrayList<>();
        int sum = 0;
        for (double d : lst) {
            rounded_lst.add((int) Math.ceil(d));
        }
        for (int i : rounded_lst) {
            sum += i * i;
        }
        return sum;
    }
}

