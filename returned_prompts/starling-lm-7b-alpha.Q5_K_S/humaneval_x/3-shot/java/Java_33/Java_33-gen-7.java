        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.add(Collections.min(l));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

