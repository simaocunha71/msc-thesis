    vector<string> letter_grades;
    for(int i=0; i<grades.size(); i++){
        if(grades[i]>=4.0){
            letter_grades.push_back("A+");
        }
        else if(grades[i]>3.7){
            letter_grades.push_back("A");
        }
        else if(grades[i]>3.3){
            letter_grades.push_back("A-");
        }
        else if(grades[i]>3.0){
            letter_grades.push_back("B+");
        }
        else if(grades[i]>2.7){
            letter_grades.push_back("B");
        }
        else if(grades[i]>2.3){
            letter_grades.push_back("B-");
        }
        else if(grades[i]>2.0){
            letter_grades.push_back("C+");
        }
        else if(grades[i]>1.7){
            letter_grades.push_back("C");
        }
        else if(grades[i]>1.3){
            letter_grades.push_back("C-");
        }
        else if(grades[i]>1.0){
            letter_grades.push_back("D+");
        }
        else if(grades[i]>0.7){
            letter_grades.push_back("D");
        }
        else if(grades[i]>0.0){
            letter_grades.push_back("D-");
        }
        else if(grades[i]==0.0){
            letter_grades.push_back("E");
        }
    }
    return letter_grades;
}
int main(){
    vector<float> grades={4.0, 3, 1.7, 2, 3.5};
    vector<string> letter_grades=numerical_letter_grade(grades);
    for(int i=0; i<letter_grades.size(); i++){
        printf("%s\n", letter_grades[i].c_str());
   