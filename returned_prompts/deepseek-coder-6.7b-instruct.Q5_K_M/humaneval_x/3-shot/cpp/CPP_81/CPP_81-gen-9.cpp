    vector<string> letter_grades;
    for(auto g : grades){
        if(g == 4.0) {
            letter_grades.push_back("A+");
        } else if(g >= 3.7) {
            letter_grades.push_back("A");
        } else if(g >= 3.3) {
            letter_grades.push_back("A-");
        } else if(g >= 3.0) {
            letter_grades.push_back("B+");
        } else if(g >= 2.7) {
            letter_grades.push_back("B");
        } else if(g >= 2.3) {
            letter_grades.push_back("B-");
        } else if(g >= 2.0) {
            letter_grades.push_back("C+");
        } else if(g >= 1.7) {
            letter_grades.push_back("C");
        } else if(g >= 1.3) {
            letter_grades.push_back("C-");
        } else if(g >= 1.0) {
            letter_grades.push_back("D+");
        } else if(g >= 0.7) {
            letter_grades.push_back("D");
        } else if(g >= 0.0) {
            letter_grades.push_back("D-");
        } else {
            letter_grades.push_back("E");
        }
    }
    return letter_grades;
}


