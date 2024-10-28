        if (lst.size() < 2) {
            return Optional.empty();
        }
        int min = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;
        for (int num : lst) {
            if (num < min) {
                secondMin = min;
                min = num;
            } else if (num > min && num < secondMin) {
                secondMin = num;
            }
        }
        return (secondMin == Integer.MAX_VALUE) ? Optional.empty() : Optional.of(secondMin);
    }
}

*/

//src/main/java/com/kodilla/optional/OptionalExample.java
package com.kodilla.optional;

import com.kodilla.optional.homework.Student;
import com.kodilla.optional.homework.Task;

import java.util.Optional;

public class OptionalExample {
    public static void main(String[] args) {
        Student john = new Student("John Smith", null);
        Optional<Task> optionalTask = Optional.ofNullable(john.getTask());

        String nameOfTask =
                optionalTask.orElse(new Task("<none>", null)).getName();

        System.out.println(nameOfTask);
    }
}

//src/main/java/com/kodilla/stream/homework/Course.java
package com.kodilla.stream.homework;

import java.util.ArrayList;
import java.util.List;

public class Course {
    private String name;
    private List<Student> students = new ArrayList<>();

    public Course(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        students.add(student);
    }
}

//src/main/java/com/kodilla/stream/homework/Student.java
package com.kodilla.