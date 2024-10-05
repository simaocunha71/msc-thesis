        List<Integer> result = new ArrayList<>();
        Collections.sort(l);

        result.add(l.get(0));
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i).equals(result.get(result.size() - 1))) {
                continue;
            }
            result.add(l.get(i));
        }
        return result;
    }
}

