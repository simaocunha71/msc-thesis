    var letter_grades = make([]string, 0)

    for _, grade := range grades {
        if grade >= 4.0 {
            letter_grades = append(letter_grades, "A+")
        }else if grade > 3.7 && grade < 4.0 {
            letter_grades = append(letter_grades, "A")
        }else if grade > 3.3 && grade <= 3.7 {
            letter_grades = append(letter_grades, "A-")
        }else if grade > 3.0 && grade <= 3.3 {
            letter_grades = append(letter_grades, "B+")
        }else if grade > 2.7 && grade <= 3.0 {
            letter_grades = append(letter_grades, "B")
        }else if grade > 2.3 && grade <= 2.7 {
            letter_grades = append(letter_grades, "B-")
        }else if grade > 2.0 && grade <= 2.3 {
            letter_grades = append(letter_grades, "C+")
        }else if grade > 1.7 && grade <= 2.0 {
            letter_grades = append(letter_grades, "C")
        }else if grade > 1.3 && grade <= 1.7 {
            letter_grades = append(letter_grades, "C-")
        }else if grade > 1.0 && grade <= 1.3 {
            letter_grades = append(letter_grades, "D+")
        }else if grade > 0.7 && grade <= 1.0 {
            letter_grades = append(letter_grades, "D")
        }else if grade <= 0.7 {
            letter_grades = append(letter_grades, "D-")
        }else{
            letter_grades = append(letter_grades, "E")
        }
    }
    return letter_grades
}



