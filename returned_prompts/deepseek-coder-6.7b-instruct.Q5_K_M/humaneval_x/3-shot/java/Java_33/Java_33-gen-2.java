        List<Integer> sorted_third = new ArrayList<>();
        List<Integer> third = new ArrayList<>();

        for  (int i = 0; i < l.size(); i++) {
            if  ((i + 1) % 3 == 0) {
                third.add(l.get(i));
             }
         }

        Collections.sort(third);

        int j = 0;
        for  (int i = 0; i < l.size(); i++) {
            if  ((i + 1) % 3 == 0) {
                sorted_third.add(third.get(j++));
             } else {
                sorted_third.add(l.get(i));
             }
         }

        return sorted_third;
     }
}

