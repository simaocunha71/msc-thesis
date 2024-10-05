        if(txt.isEmpty()){
            return false;
        }

        char lastChar = txt.charAt(txt.length()-1);
        if(Character.isLetter(lastChar)){
            if(txt.length() == 1){
                return true;
            }
            else if(txt.charAt(txt.length()-2) == ' '){
                return true;
            }
        }
        return false;
    }
}

The function first checks if the string is empty. If so, it returns false.
Then, it gets the last character of the string and checks if it is a letter.
If it is, it checks if it is the only character in the string or if the second to last character is a space (indicating it's not a part of a word). If it's the only character or the second to last character is a space, the function returns true; otherwise, it returns false.
*/

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.checkIfLastCharIsALetter("apple pie")); // false
        System.out.println(solution.checkIfLastCharIsALetter("apple pi e")); // true
        System.out.println(solution.checkIfLastCharIsALetter("apple pi e ")); // false
        System.out.println(solution.checkIfLastCharIsALetter("")); // false
    }
}

// This program will print:
// false
// true
// false
// false
// indicating that the function works as expected.

/*
The time complexity of this solution is O(1), which means it operates in constant time. The space complexity is also O(1), which means it uses constant space.
*/

// The solution is correct because it checks if the last character in the string is an alphabetical character and is not part of a word. It does this by checking the last character and the second to last character (if it exists) in the string. If the last character is a letter and the second to last character is a space, it returns true; otherwise, it returns false.
// The solution is efficient