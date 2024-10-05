        List<Integer> result = new ArrayList<>();
        while (!lst.isEmpty()) {
            int min = Collections.min(lst);
            int max = Collections.max(lst);
            result.add(min);
            result.add(max);
            lst.remove(Integer.valueOf(min));
            lst.remove(Integer.valueOf(max));
        }
        return result;
    }
}

