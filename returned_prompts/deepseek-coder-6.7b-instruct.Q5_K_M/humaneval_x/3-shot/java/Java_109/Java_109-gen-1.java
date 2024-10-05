        int n = arr.size();
        if(n == 0) return true;
        int index = -1;
        for(int i = n - 1; i > 0; i--){
            if(arr.get(i) < arr.get(i - 1)){
                index = i;
                break;
            }
        }
        if(index == -1) return true;
        for(int i = index - 1; i >= 0; i--){
            if(arr.get(i) > arr.get(index)){
                return false;
            }
        }
        if(arr.get(n - 1) <= arr.get(0)){
            for(int i = n - 1; i > index; i--){
                if(arr.get(i) < arr.get(i - 1)){
                    return false;
                }
            }
        }
        return true;
    }
}

