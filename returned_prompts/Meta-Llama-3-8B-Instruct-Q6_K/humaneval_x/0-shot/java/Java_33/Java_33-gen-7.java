    List<Integer> l = new ArrayList<Integer>();
    for(int i = 0; i < 7; i++){
        l.add(i+1);
    }
    List<Integer> result = new ArrayList<Integer>();
    for(int i = 0; i < l.size(); i++){
        if(i % 3 == 0){
            Collections.sort(Arrays.asList(l.get(i)));
            for(int j = 0; j < Collections.singletonList(l.get(i)).size(); j++){
                result.add((Integer) Collections.singletonList(l.get(i)).get(j));
            }
        }else{
            result.add(l.get(i));
        }
    }
    return result;    
}
