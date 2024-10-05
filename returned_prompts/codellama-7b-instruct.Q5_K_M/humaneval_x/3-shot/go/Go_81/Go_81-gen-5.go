    result := make([]string, len(grades))
    letter_grade_map := map[float64]string{
        4.0: "A+",
        3.7: "A",
        3.3: "A-",
        3.0: "B+",
        2.7: "B",
        2.3: "B-",
        2.0: "C+",
        1.7: "C",
        1.3: "C-",
        1.0: "D+",
        0.7: "D",
        0.0: "D-",
    }

    for i, grade := range grades{
        if grade >= 4.0{
            result[i] = letter_grade_map[4.0]
        }else if grade > 3.7{
            result[i] = letter_grade_map[3.7]
        }else if grade > 3.3{
            result[i] = letter_grade_map[3.3]
        }else if grade > 3.0{
            result[i] = letter_grade_map[3.0]
        }else if grade > 2.7{
            result[i] = letter_grade_map[2.7]
        }else if grade > 2.3{
            result[i] = letter_grade_map[2.3]
        }else if grade > 2.0{
            result[i] = letter_grade_map[2.0]
        }else if grade > 1.7{
            result[i] = letter_grade_map[1.7]
        }else if grade > 1.3{
            result[i] = letter_grade_map[1.3]
        }else if grade > 1.0{
            result[i] = letter_grade_map[1.0]
        }else if grade > 0.7{
            result[i] = letter_grade_map[0.7]
        }else if grade > 0.0{
            result[i] = letter_grade_map[0.0]
        }else{
