        for(int i=0; i<grades.size(); i++){
            if(grades.get(i) < 1.0){
                grades.set(i, "E");
            } else if(grades.get(i) < 1.3){
                grades.set(i, "D+");
            } else if(grades.get(i) < 1.7){
                grades.set(i, "D");
            } else if(grades.get(i) < 2.0){
                grades.set(i, "D