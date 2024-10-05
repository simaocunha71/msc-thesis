        List<Integer> ints = new ArrayList<>();

        for (double d : lst) {
            ints.add((int) Math.ceil(d));
        }
        int result = 0;

        for (int i : ints) {
            result += i * i;
        }
        return result;
    }
}

