        // List<String> returnList = new ArrayList<String>();
        List<String> returnList = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < paren_string.length(); i++){
            char currChar = paren_string.charAt(i);
            if(currChar == '(')
                stack.push(currChar);
            else if(currChar == ')'){
                stack.pop();
                if(stack.isEmpty())
                    returnList.add(getCurrParenString(paren_string, i));
            }
        }
        if(stack.isEmpty())
            returnList.add(getCurrParenString(paren_string, paren_string.length()));
        return returnList;
    }

    private String getCurrParenString(String paren_string, int end_idx){
        String returnString = "";
        for(int i = 0; i < end_idx; i++){
            char currChar = paren_string.charAt(i);
            if(currChar == '(')
                returnString += currChar;
            else if(currChar == ')')
                break;
            else
                returnString += currChar;
        }
        return returnString;
    }

}
