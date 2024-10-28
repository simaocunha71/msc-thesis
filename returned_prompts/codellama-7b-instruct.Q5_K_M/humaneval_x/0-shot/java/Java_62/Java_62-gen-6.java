    int len = xs.size();
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 1; i < len; i++) {
            result.add(xs.get(i) * i);
        }
        return result;
    }
}

