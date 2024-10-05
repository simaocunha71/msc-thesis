        List<Integer> rounded_lst = new ArrayList<>();
        for (double d : lst) {
            rounded_lst.add((int) Math.ceil(d));
        }

        int result = 0;
        for (int i : rounded_lst) {
            result += i * i;
        }
        return result;
    }
}

