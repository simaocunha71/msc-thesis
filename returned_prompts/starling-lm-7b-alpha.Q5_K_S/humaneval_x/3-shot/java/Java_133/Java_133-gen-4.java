        List<Integer> int_list = new ArrayList<>();
        for (double d : lst) {
            int_list.add((int) Math.ceil(d));
        }
        int result = 0;
        for (int i : int_list) {
            result += i * i;
        }
        return result;
    }
}

