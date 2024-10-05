        if (lst.size() <= 1) {
            return lst;
        }

        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        while (!lst.isEmpty()) {
            result.add(lst.remove(0));  // add minimum
            if (!lst.isEmpty()) {
                result.add(lst.remove(lst.size() - 1));  // add maximum
            }
        }
        return result;
    }
}

