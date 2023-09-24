package com.degree;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class StudentTest {

    Student a;

    @BeforeEach
    public void setup(){
        a = new Student();
    }

    @Test
    void setNomeTest() {
        a.setName("Miguel");
        assertEquals("Miguel", a.getName(), "Nome do aluno incorreto");
    }

    @Test
    void setNotaTest() {
        assertThrows(InvalidGradeException.class, () ->  a.setGrade("ATS", 49), "Nota inválida aceite");
        assertThrows(InvalidGradeException.class, () ->  a.setGrade("ATS", -620), "Nota inválida aceite");
    }

    @Test
    void incrementaNotaTest() {
        try {
            a.setGrade("ATS", 10);
            a.incrementGrade("ATS", 5);
            assertEquals(15, a.getGrade("ATS"), 0.05, "Nota inválida após incremento");
        }
        catch (InvalidGradeException e){
            fail ("NotaInvalidaException no teste incrementaNotaTest");
        }

    }
}