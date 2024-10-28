        if(arr.size() == 0) return true;
        int shift = 0;
        for(int i = 0; i < arr.size()-1; i++){
            if(arr.get(i) > arr.get(i+1)){
                shift++;
            }
        }
        if(arr.get(arr.size()-1) > arr.get(0)){
            shift++;
        }
        return shift <= 1;
    }
}

