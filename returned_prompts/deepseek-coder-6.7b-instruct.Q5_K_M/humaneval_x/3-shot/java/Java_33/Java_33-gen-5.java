        List<Integer> sortedThirds = new ArrayList<Integer>();
        for (int i = 0; i < l.size(); i++) {
            if ((i + 1) % 3 == 0) sortedThirds.add(l.get(i));
        }
        Collections.sort(sortedThirds);

        for (int i = 0, j = 0; i < l.size(); i++) {
            if ((i + 1) % 3 == 0) l.set(i, sortedThirds.get(j++));
        }
        return l;
     }
}

