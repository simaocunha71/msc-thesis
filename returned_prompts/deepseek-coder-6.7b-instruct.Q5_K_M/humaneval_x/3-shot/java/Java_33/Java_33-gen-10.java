        List<Integer> sorted = new ArrayList<>(l);
        Collections.sort(sorted);

        for  (int i = 0; i < l.size(); i++) {
            if  ((i + 1) % 3 == 0)  l.set(i, sorted.get(i));
        }
        return l;
     }
}

