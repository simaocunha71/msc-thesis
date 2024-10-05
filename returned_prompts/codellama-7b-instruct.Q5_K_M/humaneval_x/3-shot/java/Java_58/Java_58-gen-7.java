        Set<Integer> result = new HashSet<Integer>();
        for (int i : l1) {
            if (l2.contains(i)) result.add(i);
        }
        return new ArrayList<Integer>(result);
    }
}

