        if (lst.size() == 0) return lst;
        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        while (lst.size() > 0) {
            result.add(lst.remove(0));
            if (lst.size() > 0) result.add(lst.remove(lst.size() - 1));
        }
        return result;
    }
}

