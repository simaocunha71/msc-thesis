        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                List<Integer> subList = l.subList(i, i + (l.size() - i) % 3);
                Collections.sort(subList);
                result.addAll(subList);
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

