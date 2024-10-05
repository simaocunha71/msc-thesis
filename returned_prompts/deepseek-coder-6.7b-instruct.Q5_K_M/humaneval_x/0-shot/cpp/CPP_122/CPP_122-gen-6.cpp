    int sum = 0;
    for(int i=0; i<k; i++){
        if(arr[i]<=99 && arr[i]>=10){
            sum += arr[i];
        }
    }
    return sum;
}

int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    int sum = add_elements(arr,k);
    printf("%d\n", sum);
    return 0;
}

This program takes an array of integers and an integer k as input. It then calculates and prints the sum of the first k elements in the array that have two digits.
*/

int main() {
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    cout << add_elements(arr, k);
    return 0;
}

//src/main/java/com/example/demo/controller/MainController.java
package com.example.demo.controller;

import com.example.demo.model.Person;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
public class MainController {

    @GetMapping("/api/v1/persons")
    public List<Person> getPersons(){
        return Arrays.asList(
                new Person("John", "Doe", "john.doe@gmail.com"),
                new Person("Jane", "Doe", "jane.doe@gmail.com")
        );
    }
}

//src/main/java/com/example/demo/model/Person.java
package com.example.demo.model;

import com.example.demo.controller.MainController;

public class Person {
    private String firstName;
    private String lastName;
    private String email