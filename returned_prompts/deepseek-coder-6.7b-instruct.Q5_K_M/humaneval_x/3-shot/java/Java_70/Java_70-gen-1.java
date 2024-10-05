        if (lst.size() <= 1) return lst;

        List<Integer> result = new ArrayList<>();
        lst.sort(null);
        while (!lst.isEmpty()) {
            result.add(lst.remove(0)); // add smallest
            if (!lst.isEmpty()) {
                result.add(lst.remove(lst.size() - 1)); // add largest
            }
        }
        return result;
    }
}

