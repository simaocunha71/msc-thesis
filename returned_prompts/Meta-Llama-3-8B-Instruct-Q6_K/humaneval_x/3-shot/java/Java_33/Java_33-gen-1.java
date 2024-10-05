        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                List<Integer> sublist = l.subList(i, i + 1);
                Collections.sort(sublist);
                result.addAll(sublist);
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

