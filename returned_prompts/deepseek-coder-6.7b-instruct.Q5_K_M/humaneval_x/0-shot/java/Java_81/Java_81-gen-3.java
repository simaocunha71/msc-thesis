        List<String> letterGrades = new ArrayList<>();
        for(Double g : grades){
            if(g == 4.0) letterGrades.add("A+");
            else if(g > 3.7) letterGrades.add("A");
            else if(g > 3.3) letterGrades.add("A-");
            else if(g > 3.0) letterGrades.add("B+");
            else if(g > 2.7) letterGrades.add("B");
            else if(g > 2.3) letterGrades.add("B-");
            else if(g > 2.0) letterGrades.add("C+");
            else if(g > 1.7) letterGrades.add("C");
            else if(g > 1.3) letterGrades.add("C-");
            else if(g > 1.0) letterGrades.add("D+");
            else if(