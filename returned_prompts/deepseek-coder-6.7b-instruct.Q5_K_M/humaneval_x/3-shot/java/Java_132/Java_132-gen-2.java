        Stack<Character> stack = new Stack<>();
        for(char c : string.toCharArray()){
            if(c == '['){
                stack.push(c);
            } else if(!stack.isEmpty() && stack.peek() == '['){
                stack.pop();
                if(stack.isEmpty()){
                    stack.push(c);
                }
            }
        }
        return !stack.isEmpty();
    }
}

