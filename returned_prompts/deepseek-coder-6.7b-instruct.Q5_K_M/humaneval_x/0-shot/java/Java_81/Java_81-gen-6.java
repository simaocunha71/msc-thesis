        List<String> letterGrades = new ArrayList<String>();

        for(Double grade : grades){
            if(grade == 4.0)
                letterGrades.add("A+");
            else if(grade > 3.7)
                letterGrades.add("A");
            else if(grade > 3.3)
                letterGrades.add("A-");
            else if(grade > 3.0)
                letterGrades.add("B+");
            else if(grade > 2.7)
                letterGrades.add("B");
            else if(grade > 2.3)
                letterGrades.add("B-");
            else if(grade > 2.0)
                letterGrades.add("C+");
            else if(grade > 1.7)
                letterGrades.add("C");
            else if(grade > 1.3)
                letterGrades.add("C-");
            else if(grade > 1.0)
                letterGrades.add("D+");
            else if(grade > 0.7)
                letterGrades.add("D");
            else if(grade > 0.0)
                letterGrades.add("D-");
            else
                letterGrades.add("E");
        }

        return letterGrades;
    }
}


A: 
The problem in your code is that you are not properly comparing the double values. In Java, when comparing double values, it's better to use an "epsilon-comparison" as the == operator may not work due to precision errors. 

A: Here is the corrected code.

public List<String> numericalLetterGrade(List<Double> grades) {

    List<String> letterGrades = new ArrayList<String>();

    for(Double grade : grades){
        if(Math.abs(grade - 4.0) < 0.00001)
            letterGrades.add("A+");
        else if(grade > 3.7)
            letterGrades.add("A");
        else if(grade > 3.3)
            letterGrades.add("A-");
        else if(grade > 