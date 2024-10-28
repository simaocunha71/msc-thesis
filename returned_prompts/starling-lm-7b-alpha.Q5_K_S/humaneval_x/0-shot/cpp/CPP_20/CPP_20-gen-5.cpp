    def numerical_letter_grade(grades):
        grades = [round(x, 1) for x in grades]
        letter_grade_dict = {
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
            0.0: "E"
        }
        letter_grades = []
        for g in grades:
            if g in letter_grade_dict:
                letter_grades.append(letter_grade_dict[g])
            else:
                letter_grades.append("E")
        return letter_grades

# print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))




# Made By Mostafa_Khaled



```
Here is a Python program that defines a function `numerical_letter_grade` that takes a list of GPAs as input and returns a list of corresponding letter grades. The function uses a dictionary `letter_grade_dict` to map GPAs to letter grades. The dictionary is defined with the following grades and letter grades:

- 4.0: A+
- > 3.7: A
- > 3.3: A-
- > 3.0: B+
- > 2.7: B
- > 2.3: B-
- > 2.0: C+
- > 1.7: C
- > 1.3: C-
- > 1.0: D+
- > 0.7: D
- > 0.0: D-
- 0.0: E

The function first rounds each GPA in the input list to one decimal place using a list comprehension. Then, it iterates over each GPA in the rounded list and checks if it