        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            List<Integer> ints = Arrays.asList((Integer) x, (Integer) y, (Integer) z);
            Collections.sort(ints);
            return (ints.get(0) + ints.get(1)) == ints.get(2);
        }
        return false;
    }
}

