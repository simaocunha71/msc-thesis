package com.degree;

import java.util.Map;
import java.util.Objects;
import java.util.TreeMap;

public class Student {
    private String name;
    private String id;
    private Map<String, Double> grades;

    public Student() {
        this.name = "N/A";
        this.id = "N/A";
        this.grades = new TreeMap<>();
    }

    public Student(String name, String id) {
        this.name = name;
        this.id = id;
        this.grades = new TreeMap<>();
    }

    public Student(Student s) {
        this.name = s.getName();
        this.id = s.getId();
        this.grades = s.getGrades();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Map<String, Double> getGrades() {
        return grades;
    }

    public void setGrades(Map<String, Double> grades){
        this.grades = grades;
    }

    public void setGrade(String courseId, double grade) throws InvalidGradeException {
        if (grade < 0 || grade > 20) throw new InvalidGradeException();
        grades.put(courseId, grade);
    }

    public double getGrade(String courseId){
        return grades.get(courseId);
    }

    public void incrementGrade(String courseId, int value) throws InvalidGradeException {
        setGrade(courseId, getGrade(courseId) + value);
    }

    public double average(){
        return grades.values().stream().mapToDouble(x -> x).average().orElse(0.0);
    }

    @Override
    protected Student clone() {
        return new Student(this);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return Objects.equals(name, student.name) && Objects.equals(id, student.id) && Objects.equals(grades, student.grades);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, id, grades);
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", id='" + id + '\'' +
                ", grades=" + grades +
                '}';
    }
}
