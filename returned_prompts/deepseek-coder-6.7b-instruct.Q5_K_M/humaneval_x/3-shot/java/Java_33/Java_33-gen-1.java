        List<Integer> result = new ArrayList<>(l);
        List<Integer> toSort = new ArrayList<>();

        for  (int i = 0; i < l.size(); i++)  {
            if  (i % 3 == 0)  {
                toSort.add(l.get(i));
            }
        }
        Collections.sort(toSort);

        for  (int i = 0, j = 0; i < l.size(); i++)  {
            if  (i % 3 == 0)  {
                result.set(i, toSort.get(j++));
            }
        }

        return result;
     }
}

