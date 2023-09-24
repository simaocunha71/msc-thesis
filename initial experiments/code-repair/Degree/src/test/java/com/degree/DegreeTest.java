package com.degree;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DegreeTest {

    Student a, b, c;
    Degree t;

    @BeforeEach
    public void setup(){
        a = new Student("Alfredo", "A00000");
        b = new Student("Bernardo", "A00001");
        c = new Student("Carlos", "A00002");
        t = new Degree();
    }

    @Test
    void addAlunoTest() {
        t.addStudent(a);
        assertTrue(t.containsStudent("A00000"), "Aluno inserido nao se encontra na turma");
    }

    @Test
    void getAlunoTest() {
        t.addStudent(a);
        try {
            Student r = t.getStudent("A00000");
            assertEquals(a, r, "Alfredo inserido e obtido de turma nao e igual ao original");
        }
        catch (StudentDoesNotExistException e){
            fail("AlunoInexistenteException no teste getAlunoTest");
        }
    }

    @Test
    void mediaTest() {
        try {
            a.setGrade("ATS", 10);
            b.setGrade("ATS", 12);
            c.setGrade("ATS", 8);
            t.addStudent(a);
            t.addStudent(b);
            t.addStudent(c);
            assertEquals(10.0, t.average(), 0.05, "Media calculada com valor incorreto");
        }
        catch (InvalidGradeException e){
            fail("NotaInvalidaException no teste mediaException");
        }

    }


}