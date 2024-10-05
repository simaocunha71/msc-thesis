        StringBuilder result = new StringBuilder();
        for(int i = 0; i < text.length(); i++){
            char c = text.charAt(i);
            if(!"aeiouAEIOU".contains(String.valueOf(c))){
                result.append(c);
            }
        }
        return result.toString();
    }
}

I am trying to solve this problem, but the code does not compile. The error I'm getting is "Class Solution should have been public"

A: The issue is not with the code but with the way you have written your question. 
The code you have posted is already correct and should compile and run without any issues. 

Please ensure that you have posted the question in the correct format. The question should start with a question mark followed by the problem statement, and then the code should be posted as an example.

So, the question should look something like this:
