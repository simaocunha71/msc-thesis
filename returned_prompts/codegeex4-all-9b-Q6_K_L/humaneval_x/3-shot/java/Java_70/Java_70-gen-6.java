        List<Integer> result = new ArrayList<>();
        while (lst.size() > 0) {
            result.add(Collections.min(lst));
            lst.remove(Collections.min(lst));
            if (lst.size() > 0) {
                result.add(Collections.max(lst));
                lst.remove(Collections.max(lst));
            }
        }
        return result;
    }
}

