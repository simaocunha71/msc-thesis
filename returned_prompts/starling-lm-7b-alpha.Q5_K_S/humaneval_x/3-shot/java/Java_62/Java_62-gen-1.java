        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < xs.size(); i++) {
            if (i == 0) {
                result.add(xs.get(i));
            } else if (i == xs.size() - 1) {
                result.add(xs.get(i) * i);
            } else {
                result.add(xs.get(i) * i + xs.get(i + 1));
                i += 1;
            }
        }
        return result;
    }
}

