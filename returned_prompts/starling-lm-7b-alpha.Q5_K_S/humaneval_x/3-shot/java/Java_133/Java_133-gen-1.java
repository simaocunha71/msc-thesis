        List<Integer> int_lst = new ArrayList<>();
        for (double d : lst) {
            int_lst.add((int) Math.ceil(d));
        }
        return int_lst.stream().map(i -> i * i).mapToInt(i -> i).sum();
    }
}

