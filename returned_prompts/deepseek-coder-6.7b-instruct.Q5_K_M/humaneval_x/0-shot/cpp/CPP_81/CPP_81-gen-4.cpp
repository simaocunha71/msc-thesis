    vector<string> letterGrade;
    for(int i=0; i<grades.size(); i++){
        if(grades[i]==4.0){
            letterGrade.push_back("A+");
        }
        else if(grades[i]>3.7){
            letterGrade.push_back("A");
        }
        else if(grades[i]>3.3){
            letterGrade.push_back("A-");
        }
        else if(grades[i]>3.0){
            letterGrade.push_back("B+");
        }
        else if(grades[i]>2.7){
            letterGrade.push_back("B");
        }
        else if(grades[i]>2.3){
            letterGrade.push_back("B-");
        }
        else if(grades[i]>2.0){
            letterGrade.push_back("C+");
        }
        else if(grades[i]>1.7){
            letterGrade.push_back("C");
        }
        else if(grades[i]>1.3){
            letterGrade.push_back("C-");
        }
        else if(grades[i]>1.0){
            letterGrade.push_back("D+");
        }
        else if(grades[i]>0.7){
            letterGrade.push_back("D");
        }
        else if(grades[i]>0.0){
            letterGrade.push_back("D-");
        }
        else{
            letterGrade.push_back("E");
        }
    }
    return letterGrade;
}

int main(){
    vector<float> gpa = {4.0, 3, 1.7, 2, 3.5};
    vector<string> grade = numerical_letter_grade(gpa);
    for(int i=0; i<grade.size(); i++){
        printf("%s ",grade[i].c_str());
    }
    return 0;
}

*/
