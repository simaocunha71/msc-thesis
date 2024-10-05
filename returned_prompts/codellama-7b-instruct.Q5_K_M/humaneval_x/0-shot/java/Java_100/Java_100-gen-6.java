        List<Integer> ret = new ArrayList<>();
        while (n > 0) {
            ret.add(n);
            n = (n % 2 == 0) ? n + 1 : n + 2;
        }
        return ret;
    }
}
