        List<Integer> result = new ArrayList<>();
        if (lst.size() == 0) return result;

        while (lst.size() > 0) {
            if (result.size() % 2 == 0) {
                result.add(Collections.min(lst));
                lst.remove(Collections.min(lst));
            } else {
                result.add(Collections.max(lst));
                lst.remove(Collections.max(lst));
            }
        }

        return result;
    }
}

