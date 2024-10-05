        List<Integer> l_sorted = l;
        for (int i = 0; i < l.size(); i += 2) {
            Collections.sort(l_sorted);
        }
        return l_sorted;
    }
}

