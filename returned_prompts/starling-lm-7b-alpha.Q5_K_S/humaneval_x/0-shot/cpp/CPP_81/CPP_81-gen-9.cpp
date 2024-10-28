    vector<string> letter_grade;
    for(int i = 0; i < grades.size(); i++){
        if(grades[i] >= 4.0){
            letter_grade.push_back("A+");
        }
        else if(grades[i] > 3.7){
            letter_grade.push_back("A");
        }
        else if(grades[i] > 3.3){
            letter_grade.push_back("A-");
        }
        else if(grades[i] > 3.0){
            letter_grade.push_back("B+");
        }
        else if(grades[i] > 2.7){
            letter_grade.push_back("B");
        }
        else if(grades[i] > 2.3){
            letter_grade.push_back("B-");
        }
        else if(grades[i] > 2.0){
            letter_grade.push_back("C+");
        }
        else if(grades[i] > 1.7){
            letter_grade.push_back("C");
        }
        else if(grades[i] > 1.3){
            letter_grade.push_back("C-");
        }
        else if(grades[i] > 1.0){
            letter_grade.push_back("D+");
        }
        else if(grades[i] > 0.7){
            letter_grade.push_back("D");
        }
        else if(grades[i] > 0.0){
            letter_grade.push_back("D-");
        }
        else if(grades[i] == 0.0){
            letter_grade.push_back("E");
        }
    }
    return letter_grade;
}

int main(){
    vector<float> grades = {3, 4.0, 2.7, 1.7, 3.5};
    for(int i = 0; i < numerical_letter_grade(grades).size(); i++){
        printf("%s ", numerical_letter_grade(grades)[i].