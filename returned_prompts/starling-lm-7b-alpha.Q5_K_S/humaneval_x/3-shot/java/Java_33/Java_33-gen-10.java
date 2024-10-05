        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 != 0) result.add(l.get(i));
            else result.add(Collections.sort(new ArrayList<>(l.subList(i, i + 1))).get(0));
        }
        return result;
    }
}

