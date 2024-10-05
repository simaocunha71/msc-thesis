        //TODO: YOUR CODE HERE
        List<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < l.size(); i++){
            if(i % 2 == 0){
                list.add(l.get(i));
            }
            else{
                list.add(Collections.sort(l.subList(i, i+1)));
            }
        }
        return list;
    }
}
