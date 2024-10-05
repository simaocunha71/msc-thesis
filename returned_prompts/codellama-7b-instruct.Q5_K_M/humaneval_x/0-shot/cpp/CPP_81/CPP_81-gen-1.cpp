  for (int i = 0; i < grades.size(); i++){
    if (grades[i] >= 4){
      grades[i] = "A+";
    }else if (grades[i] >= 3.7){
      grades[i] = "A";
    }else if (grades[i] >= 3.3){
      grades[i] = "A-";
    }else if (grades[i] >= 3.0){
      grades[i] = "B+";
    }else if (grades[i] >= 2.7){
      grades[i] = "B";
    }else if (grades[i] >= 2.3){
      grades[i] = "B-";
    }else if (grades[i] >= 2.0){
      grades[i] = "C+";
    }else if (grades[i] >= 1.7){
      grades[i] = "C";
    }else if (grades[i] >= 1.3){
      grades[i] = "C-";
    }else if (grades[i] >= 1.0){
      grades[i] = "D+";
    }else if (grades[i] >= 0.7){
      grades[i] = "D";
    }else if (grades[i] >= 0.0){
      grades[i] = "D-";
    }else{
      grades[i] = "E";
    }
  }
  return grades;
}

int main(){
  vector<float> grades = {4.0, 3, 1.7, 2, 3.5};
  vector<string> letter_grades = numerical_letter_grade(grades);
  for (int i = 0; i < letter_grades.size(); i++){
    cout << letter_grades[i] << endl;
  }
}

