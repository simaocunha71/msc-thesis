        List<Integer> result = new ArrayList<>();
        if (lst.size() == 0) {
            return result;
        }
        Collections.sort(lst);
        while (!lst.isEmpty()) {
            result.add(lst.remove(0));
            if (!lst.isEmpty()) {
                int minIndex = 0;
                for (int i = 1; i < lst.size(); i++) {
                    if (lst.get(i) < lst.get(minIndex)) {
                        minIndex = i;
                    }
                }
                result.add(lst.remove(minIndex));
            }
        }
        return result;
    }
}

