        List<Integer> even_indices_values = new ArrayList<>();
        for  (int i = 0; i < l.size(); i += 2) {
            even_indices_values.add(l.get(i));
        }
        Collections.sort(even_indices_values);

        List<Integer> result = new ArrayList<>();
        int j = 0;
        for  (int i = 0; i < l.size(); i++) {
            if  (i % 2 == 0) {
                result.add(even_indices_values.get(j++));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
     }
}

