        Collections.sort(l);
        double median;
        int n = l.size();
        if (n % 2 != 0)
            median = (double) l.get(n/2);
        else
            median = (double) (l.get((n-1)/2) + l.get(n/2))/2.0;
        return median;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        List<Integer> list = Arrays.asList(3, 1, 2, 4, 5);
        System.out.println(sol.median(list));
        List<Integer> list2 = Arrays.asList(-10, 4, 6, 1000, 10, 20);
        System.out.println(sol.median(list2));
    }
}

//src/main/java/com/example/demo/StudentService.java
package com.example.demo;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class StudentService {
	
	@Autowired
	private StudentRepository repo;
	
	public List<Student> listAll(){
		return repo.findAll();
	}
	
	public void save(Student student) {
		repo.save(student);
	}
	
	public Student get(Long id) {
		return repo.findById(id).get();
	}
	
	public void delete(Long id) {
		repo.deleteById(id);
	}
	
}

//src/main/java/com/example/demo/controller/StudentController.java
package com.example.demo.controller;

import java.util.List;
import java.util.NoSuchElementException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import