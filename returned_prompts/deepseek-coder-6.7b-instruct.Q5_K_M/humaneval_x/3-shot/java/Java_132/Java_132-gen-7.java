        Stack<Character> stack = new Stack<>();
        for(char c : string.toCharArray()){
            if(c == '['){
                stack.push(c);
            }else{
                if(stack.isEmpty()){
                    return false;
                }
                if(stack.peek() == '['){
                    stack.pop();
                }else{
                    while(!stack.isEmpty() && stack.peek() != '['){
                        stack.pop();
                    }
                    if(stack.isEmpty()){
                        return false;
                    }
                }
            }
        }
        return !stack.isEmpty();
    }
}

