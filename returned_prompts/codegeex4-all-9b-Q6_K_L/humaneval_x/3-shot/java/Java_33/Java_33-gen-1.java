        List<Integer> sorted = new ArrayList<>(l);
        Collections.sort(sorted);
        for (int i = 0; i < l.size(); i += 3) {
            l.set(i, sorted.get(i));
        }
        return l;

    }
}

