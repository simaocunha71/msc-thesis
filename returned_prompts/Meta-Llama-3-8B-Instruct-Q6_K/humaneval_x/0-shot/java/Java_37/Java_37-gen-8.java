    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> l2 = new ArrayList<>();
        for(int i = 0; i < l.size(); i++){
            if(i % 2 == 0){
                l2.add(i, Collections.sort(l.subList(i, i+1)).get(0));
            } else {
                l2.add(i, l.get(i));
            }
        }
        return l2;
    }  // This solution is using the List Interface and the subList function from the ArrayList class to sort the even indices.

B:
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> l2 = new ArrayList<>();
        for(int i = 0; i < l.size(); i++){
            if(i % 2 == 0){
                l2.add(i, Collections.min(l.subList(i, i+1)));
            } else {
                l2.add(i, l.get(i));
            }
        }
        return l2;
    }  // This solution is using the List Interface and the subList function from the ArrayList class to find the smallest value in the even indices.

C:
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> l2 = new ArrayList<>();
        for(int i = 0; i < l.size(); i++){
            if(i % 2 == 0){
                l2.add(i, Collections.max(l.subList(i, i+1)));
            } else {
                l2.add(i, l.get(i));
            }
        }
        return l2;
    }  // This solution is using the List Interface and the subList function from the ArrayList class to find the largest value in the even indices.

D:
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> l2 = new ArrayList<>();
        for(int i = 0; i < l.size(); i++){
            if(i % 2 == 0){
                l2.add(i, l.get(i));
            } else {
                l2.add(i, l.get(i));
            }
        }
        return l2;
    }  // This solution is not doing anything with the even indices. It's just copying the list. It's not the correct solution.

E:
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> l2 = new ArrayList<>();
        for(int i = 0; i < l.size(); i++){
            if