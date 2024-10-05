        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        while (!lst.isEmpty()) {
            result.add(lst.remove(0)); // Adds minimum
            if (!lst.isEmpty()) {
                result.add(lst.remove(lst.size() - 1)); // Adds maximum
            }
        }
        return result;
    }
}

