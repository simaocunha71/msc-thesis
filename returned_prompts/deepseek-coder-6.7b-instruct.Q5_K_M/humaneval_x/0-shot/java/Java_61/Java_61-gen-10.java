        Stack<Character> stack = new Stack<Character>();

        for(int i = 0; i < brackets.length(); i++){
            char c = brackets.charAt(i);

            if(c == '('){
                stack.push(c);
            } else if(c == ')'){
                if(stack.isEmpty()){
                    return false;
                }
                if(stack.peek() == '('){
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }
        }

        return stack.isEmpty();
    }
}

