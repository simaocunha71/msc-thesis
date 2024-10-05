        List<Integer> squared_integers = new ArrayList<>();
        for (double d : lst) {
            squared_integers.add((int) Math.ceil(d));
        }
        int result = 0;
        for (int i : squared_integers) {
            result += i * i;
        }
        return result;
    }
}

