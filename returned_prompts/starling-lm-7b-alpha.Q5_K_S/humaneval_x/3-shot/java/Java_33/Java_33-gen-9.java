        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 != 0) {
                result.add(l.get(i));
            } else {
                result.add(Collections.frequency(l, l.get(i)) - 1);
            }
        }
        return result;
    }
}

