    vector<string> letter_grades;
    for(int i=0;i<grades.size();i++)
    {
        float gpa = grades[i];
        if(gpa >= 4.0)
            letter_grades.push_back("A+");
        else if(gpa > 3.7)
            letter_grades.push_back("A");
        else if(gpa > 3.3)
            letter_grades.push_back("A-");
        else if(gpa > 3.0)
            letter_grades.push_back("B+");
        else if(gpa > 2.7)
            letter_grades.push_back("B");
        else if(gpa > 2.3)
            letter_grades.push_back("B-");
        else if(gpa > 2.0)
            letter_grades.push_back("C+");
        else if(gpa > 1.7)
            letter_grades.push_back("C");
        else if(gpa > 1.3)
            letter_grades.push_back("C-");
        else if(gpa > 1.0)
            letter_grades.push_back("D+");
        else if(gpa > 0.7)
            letter_grades.push_back("D");
        else
            letter_grades.push_back("E");
    }
    return letter_grades;
}
// Example usage:
int main() {
    vector<float> grades = {4.0, 3.0, 1.7, 2.0, 3.5};
    vector<string> letter_grades = numerical_letter_grade(grades);
    for(string grade : letter_grades) {
        cout << grade << endl;
    }
    return 0;
}