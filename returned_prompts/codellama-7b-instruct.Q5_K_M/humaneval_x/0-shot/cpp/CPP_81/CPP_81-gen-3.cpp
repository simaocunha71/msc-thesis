    vector<string> grade_vector;
    for (int i = 0; i < grades.size(); i++){
        if (grades[i] >= 4.0){
            grade_vector.push_back("A+");
        }
        else if (grades[i] > 3.7){
            grade_vector.push_back("A");
        }
        else if (grades[i] > 3.3){
            grade_vector.push_back("A-");
        }
        else if (grades[i] > 3.0){
            grade_vector.push_back("B+");
        }
        else if (grades[i] > 2.7){
            grade_vector.push_back("B");
        }
        else if (grades[i] > 2.3){
            grade_vector.push_back("B-");
        }
        else if (grades[i] > 2.0){
            grade_vector.push_back("C+");
        }
        else if (grades[i] > 1.7){
            grade_vector.push_back("C");
        }
        else if (grades[i] > 1.3){
            grade_vector.push_back("C-");
        }
        else if (grades[i] > 1.0){
            grade_vector.push_back("D+");
        }
        else if (grades[i] > 0.7){
            grade_vector.push_back("D");
        }
        else if (grades[i] > 0.0){
            grade_vector.push_back("D-");
        }
        else if (grades[i] < 0.0){
            grade_vector.push_back("E");
        }
    }
    return grade_vector;
}

int main(){
    vector<float> grades_vector;
    grades_vector.push_back(4.0);
    grades_vector.push_back(3.0);
    grades_vector.push_back(1.7);
