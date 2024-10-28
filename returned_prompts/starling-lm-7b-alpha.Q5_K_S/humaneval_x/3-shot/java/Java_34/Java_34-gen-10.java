        List<Integer> result = new ArrayList<>();
        TreeSet<Integer> set = new TreeSet<>();
        for (int i : l) {
            set.add(i);
        }
        for (int i : set) {
            result.add(i);
        }
        return result;
    }
}

