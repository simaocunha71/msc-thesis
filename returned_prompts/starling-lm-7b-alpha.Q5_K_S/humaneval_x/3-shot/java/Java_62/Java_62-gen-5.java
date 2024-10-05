        List<Integer> result = new ArrayList<>();
        if (xs.size() == 0) {
            return result;
        }
        result.add(xs.get(0));
        for (int i = 0; i < xs.size() - 1; i++) {
            result.add(i + 2, (xs.get(i + 1) + xs.get(i) * (i + 1)));
        }
        return result;
    }
}

