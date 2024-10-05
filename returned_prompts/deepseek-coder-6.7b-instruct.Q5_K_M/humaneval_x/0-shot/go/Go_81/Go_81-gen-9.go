
    // Initialize an empty list to store the letter grades
    var letterGrades []string

    // Iterate over the list of GPAs
    for _, gpa := range grades {

        // Use a switch statement to determine the letter grade
        switch {
        case gpa == 4.0:
            letterGrades = append(letterGrades, "A+")
        case gpa > 3.7:
            letterGrades = append(letterGrades, "A")
        case gpa > 3.3:
            letterGrades = append(letterGrades, "A-")
        case gpa > 3.0:
            letterGrades = append(letterGrades, "B+")
        case gpa > 2.7:
            letterGrades = append(letterGrades, "B")
        case gpa > 2.3:
            letterGrades = append(letterGrades, "B-")
        case gpa > 2.0:
            letterGrades = append(letterGrades, "C+")
        case gpa > 1.7:
            letterGrades = append(letterGrades, "C")
        case gpa > 1.3:
            letterGrades = append(letterGrades, "C-")
        case gpa > 1.0:
            letterGrades = append(letterGrades, "D+")
        case gpa > 0.7:
            letterGrades = append(letterGrades, "D")
        case gpa > 0.0:
            letterGrades = append(letterGrades, "D-")
        default:
            letterGrades = append(letterGrades, "E")
        }
    }

    // Return the list of letter grades
    return letterGrades
}


// The function is defined in terms of the list of GPAs. 
// It iterates over the list, converts each GPA into a letter grade using a switch statement, 
// and appends the letter grade to a new list. 
// The function then returns the new list of letter grades.

// The function uses a switch statement to convert each GPA into a letter grade 
// based on the given table. 
// If