        List<Integer> evens = new ArrayList<>();
        for  (int i = 0; i < l.size(); i += 2) {
            evens.add(l.get(i));
        }
        Collections.sort(evens);

        List<Integer> result = new ArrayList<>();
        int e = 0;
        for  (int i = 0; i < l.size(); i++) {
            if  (i % 2 == 0) {
                result.add(evens.get(e++));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
     }
}

