        List<Integer> result = new ArrayList<>();
        Collections.sort(lst);
        int min = lst.get(0);
        while (!lst.isEmpty()) {
            result.add(min);
            lst.remove((Integer) min);
            if (!lst.isEmpty()) {
                min = Collections.max(lst);
                lst.remove((Integer) min);
            }
        }
        return result;
    }
}

