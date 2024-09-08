    vector<string> letter_grades;
    for(auto i:grades){
        if(i>=4.0) letter_grades.push_back("A+");
        else if(i>3.7) letter_grades.push_back("A");
        else if(i>3.3) letter_grades.push_back("A-");
        else if(i>3.0) letter_grades.push_back("B+");
        else if(i>2.7) letter_grades.push_back("B");
        else if(i>2.3) letter_grades.push_back("B-");
        else if(i>2.0) letter_grades.push_back("C+");
        else if(i>1.7) letter_grades.push_back("C");
        else if(i>1.3) letter_grades.push_back("C-");
        else if(i>1.0) letter_grades.push_back("D+");
        else if(i>0.7) letter_grades.push_back("D");
        else if(i>0.0) letter_grades.push_back("D-");
        else letter_grades.push_back("E");
    }
    return letter_grades;
}
int main(){
    vector<float> grades = {4.0, 3.0, 1.7, 2.0, 3.5};
    vector<string> result = numerical_letter_grade(grades);
    for(auto i:result) cout<<i<<endl;
    return 0;
}
C:
    {
        return 0;
    }
}
D:
    {
        return 0;
    }
E:
    {
        return 0;
    }
F:
    {
        return 0;
    }
G:
    {
        return 0;
    }
H:
    {
        return 0;
    }
I:
    {
        return 0;
    }
J:
    {
        return 0;
    }
K:
    {
        return 0;
    }
L:
    {
        return 0;
    }
M:
    {
        return 0;
    }
N:
    {
        return 0;
    }
O:
    {
        return 0;
    }
P:
    {
        return 0;
    }
