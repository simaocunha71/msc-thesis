        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0) result.add(lst.get(i));
        }
        for (int i = lst.size() - 1; i >= 0; i--) {
            if (i % 2 == 1) result.add(lst.get(i));
        }
        return result;
    }
}

