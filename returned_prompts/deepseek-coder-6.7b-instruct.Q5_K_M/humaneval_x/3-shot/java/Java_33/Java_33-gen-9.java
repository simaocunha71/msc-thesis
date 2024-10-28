        List<Integer> sorted_third = new ArrayList<>();
        for(int i = 0; i < l.size(); i++) {
            if(i % 3 == 0) {
                sorted_third.add(l.get(i));
            }
        }
        Collections.sort(sorted_third);

        for(int i = 0, j = 0; i < l.size(); i++) {
            if(i % 3 == 0) {
                l.set(i, sorted_third.get(j++));
            }
        }
        return l;
     }
}

