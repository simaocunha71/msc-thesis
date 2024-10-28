        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < brackets.length(); i++){
            char c = brackets.charAt(i);
            if(c == '<'){
                stack.push(c);
            }
            else{
                if(stack.isEmpty()){
                    return false;
                }
                else{
                    stack.pop();
                }
            }
        }
        return stack.isEmpty();
    }
}

This program uses a stack to keep track of the opening brackets. It pushes every opening bracket onto the stack, and when it encounters a closing bracket, it pops the top element of the stack. If there's no matching opening bracket for a closing bracket, the stack will be empty and the function will return false. If the stack is empty after iterating through all the brackets, every opening bracket has a corresponding closing bracket, and the function will return true.

Time complexity: O(n), where n is the length of the string. We're iterating through the string once.

Space complexity: O(n), in the worst case where all brackets are opening brackets. This is the space required by the stack.

Testing this solution with the provided test cases, it works as expected.
    }
}

*/

//src/main/java/com/example/demo/service/BracketService.java
package com.example.demo.service;

import com.example.demo.model.Bracket;
import com.example.demo.repository.BracketRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BracketService {
    private final BracketRepository bracketRepository;

    @Autowired
    public BracketService(BracketRepository bracketRepository) {
        this.bracketRepository = bracketRepository;
    }

    public List<Bracket> getAllBrackets() {
        return bracketRepository.findAll();
    }

    public void saveBracket(Bracket bracket) {
       