    for (int i=0; i<grades.size(); i++){
        if (grades[i]==0){
            grades[i] = "E";
        } else if (grades[i]>0 && grades[i]<=3.7){
            grades[i] = "A";
        } else if (grades[i]>3.7 && grades[i]<=3.3){
            grades[i] = "A-";
        } else if (grades[i]>3.3 && grades[i]<=3){
            grades[i] = "B+";
        } else if (grades[i]>3 && grades[i]<=2.7){
            grades[i] = "B";
        } else if (grades[i]>2.7 && grades[i]<=2.3){
            grades[i] = "B-";
        } else if (grades[i]>2.3 && grades[i]<=2){
            grades[i] = "C+";
        } else if (grades[i]>2 && grades[i]<=1.7){
            grades[i] = "C";
        } else if (grades[i]>1.7 && grades[i]<=1.3){
            grades[i] = "C-";
        } else if (grades[i]>1.3 && grades[i]<=1){
            grades[i] = "D+";
        } else if (grades[i]>1 && grades[i]<=0.7){
            grades[i] = "D";
        } else if (grades[i]>0.7 && grades[i]<=0){
            grades[i] = "D-";
        }
    }
    return grades;
}


int main() {
    vector<float> grades = {4, 3, 1.7, 2, 3.5};
    vector<string> grade_vector = numerical_letter_grade(grades);
    for (int i