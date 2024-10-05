        List<Integer> result = null;
        List<Integer> even_nodes = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0) {
                even_nodes.add(value);
            }
        }
        if (even_nodes.size() == 0) {
            return result;
        }
        Collections.sort(even_nodes);
        result = new ArrayList<>();
        result.add(even_nodes.get(0));
        result.add(even_nodes.indexOf(even_nodes.get(0)));
        return result;
    }
}

