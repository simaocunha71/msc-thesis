        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            result.add(l.get(i));
            if (i % 2 == 0) {
                Collections.sort(result);
            }
        }
        return result;
    }
}

