        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < xs.size(); i++) {
            if (i == 0) {
                result.add(xs.get(i));
            } else {
                result.add(xs.get(i) * (i));
            }
        }
        return result;
    }
}

