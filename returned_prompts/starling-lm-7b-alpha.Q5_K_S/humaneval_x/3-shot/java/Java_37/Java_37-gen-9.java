        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            result.add(l.get(i));
        }
        Collections.sort(result);
        for (int i = 1; i < l.size(); i += 2) {
            result.add(l.get(i));
        }
        return result;
    }
}

