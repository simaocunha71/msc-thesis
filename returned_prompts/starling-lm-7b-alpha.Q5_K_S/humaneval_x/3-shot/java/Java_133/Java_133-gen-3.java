        List<Integer> rounded_lst = new ArrayList<>();
        for (double d : lst) {
            rounded_lst.add(Math.round(d));
        }
        int result = 0;
        for (int i : rounded_lst) {
            result += i * i;
        }
        return result;
    }
}

