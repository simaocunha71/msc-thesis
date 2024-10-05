        List<Integer> result = new ArrayList<>();
        while (!lst.isEmpty()) {
            result.add(Collections.min(lst));
            lst.remove(Collections.min(lst));
            if (!lst.isEmpty()) {
                result.add(Collections.max(lst));
                lst.remove(Collections.max(lst));
            }
        }
        return result;
    }
}

