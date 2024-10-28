        int counter = 0;
        for(char c : brackets.toCharArray()){
            if(c == '<'){
                counter++;
            } else if(c == '>'){
                counter--;
                if(counter < 0){
                    return false;
                }
            }
        }
        return counter == 0;
    }
}

