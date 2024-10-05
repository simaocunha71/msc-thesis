        List<Integer> rounded_lst = new ArrayList<>();
        for (double d : lst) {
            rounded_lst.add(Math.round(d));
        }
        int sum = 0;
        for (int i : rounded_lst) {
            sum += i * i;
        }
        return sum;
    }
}

