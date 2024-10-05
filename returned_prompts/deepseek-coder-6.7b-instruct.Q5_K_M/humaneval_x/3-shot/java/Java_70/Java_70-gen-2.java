        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        while (!lst.isEmpty()) {
            result.add(lst.remove(0)); // take smallest
            if (!lst.isEmpty()) {
                result.add(lst.remove(lst.size() - 1)); // take largest
            }
        }
        return result;
     }
}

