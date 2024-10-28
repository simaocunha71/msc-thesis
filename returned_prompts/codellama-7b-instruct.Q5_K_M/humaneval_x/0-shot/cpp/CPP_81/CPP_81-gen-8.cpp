    return vector<string>{"A+"};
}

int main(){
    vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
    vector<string> grades = numerical_letter_grade(grades);
    for(int i=0; i < grades.size(); i++){
        printf("%s\n", grades[i].c_str());
    }
}
