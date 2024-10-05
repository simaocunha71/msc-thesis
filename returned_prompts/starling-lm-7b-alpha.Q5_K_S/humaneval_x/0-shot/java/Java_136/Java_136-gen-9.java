    Optional<Integer> a = Optional.empty();
    Optional<Integer> b = Optional.empty();

    for(int i:lst){
        if(i<0 && a.isEmpty()){
            a = Optional.of(i);
        }
        else if(i<0){
            if(a.get()<i){
                a