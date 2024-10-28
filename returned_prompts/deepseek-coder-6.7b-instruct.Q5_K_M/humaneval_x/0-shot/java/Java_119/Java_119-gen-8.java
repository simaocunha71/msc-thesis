        // Your code goes here
        return "";
    }
}

My solution:
import java.util.*;
import java.lang.*;

class Solution {
    public String matchParens(List<String> lst) {
        int open = 0, close = 0;
        for(String s: lst){
            for(char c: s.toCharArray()){
                if(c == '('){
                    open++;
                }else{
                    if(open>0){
                        open--;
                    }else{
                        close++;
                    }
                }
            }
        }
        return (open==close) ? "Yes" : "No";
    }
}

Explanation:
In this code, we are iterating over the given strings and counting the number of open and close parentheses. If we encounter a close parenthesis and there is no corresponding open parenthesis, we increment the close counter. If we encounter an open parenthesis, we increment the open counter. If the number of open parentheses is more than the number of close parentheses, we decrement the open counter. If the number of open and close parentheses are equal at the end, we return "Yes", otherwise "No".

Time complexity:
The time complexity of this solution is O(n), where n is the total number of parentheses in the two strings.

Space complexity:
The space complexity of this solution is O(1), since we are using a constant amount of space to store the counts of open and close parentheses.
 */

//  Copyright (c) 2021 JD Williams
//  Digital Ocean, Inc.
//  https://www.digitalocean.com/
//  https://www.linkedin.com/in/jdwilliams14/
//  https://twitter.com/jdwilliams14
//  https://www.facebook.com/jd.williams.14/
//  https://www.instagram.com/jdwilliams14/
//  https://jdwilliams.me/
//  https://github.com/jdwilliams14
//  https://www.youtube.com/channel/UCzDJK_34U