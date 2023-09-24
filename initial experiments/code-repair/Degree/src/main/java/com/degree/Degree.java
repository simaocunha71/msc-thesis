package com.degree;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;

public class Degree {

    private List<Student> students;

    public Degree(){
        students = new ArrayList<>();
    }

    public Degree(List<Student> newStudents){
        this.setStudents(newStudents);
    }

    public Degree(Degree t){
        this(t.getStudents());
    }

    public void setStudents(List<Student> newStudents){
        students = newStudents.stream().map(Student::clone).collect(Collectors.toList());
    }

    public List<Student> getStudents(){
        return students.stream().map(Student::clone).collect(Collectors.toList());
    }

    public void addStudent(Student s){
        if (!students.contains(s)) students.add(s.clone());
    }

    public boolean containsStudent(String id) {
        return students.stream().filter(x -> x.getId().equals(id)).count() > 0;
    }

    public void removeStudent(String id) throws StudentDoesNotExistException {
        Iterator<Student> it = students.iterator();
        boolean removed = false;
        while (it.hasNext() && !removed){
            Student student = it.next();
            if (student.getId().equals(id)){
                it.remove();
                removed = true;
            }
        }
        if (!removed) throw new StudentDoesNotExistException();
    }

    public Student getStudent(String id) throws StudentDoesNotExistException {
         return students.stream().filter(x -> x.getId().equals(id)).findFirst().orElseThrow(() -> new StudentDoesNotExistException()).clone();
    }

    public double average(){
        double avg = 0.0;
        for (Student s : students){
            avg += s.average();
        }
        return avg / students.size();
    }

    public List<Student> failed(){
        List<Student> r = new ArrayList<>();
        for (Student s : students) {
            if (s.average() < 10) r.add(s.clone());
        }
        return r;
    }


    public List<Student> merit() {
        List<Student> r = new ArrayList<>();
        for (Student s : students) {
            // Only students with average above 10
            // classifications go from 0 to 20
            if (s.average() > 10) {
                // Less than 3 fails
                int fails = 0;
                for (Double d : s.getGrades().values()){
                    if (d < 10) fails = fails + 1;
                }
                if (fails < 3) r.add(s.clone());
            }
        }
        // Sorted by average
        Comparator<Student> c = (a1, a2) -> {
            double diff = a1.average() - a2.average();
            if (diff > 0.05) return -1;
            if (diff < -0.05) return 1;
            return 0;
        };
        r.sort(c);
        return r;
    }

}
