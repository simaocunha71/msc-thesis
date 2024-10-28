        if(s.length() < 3){
            return false;
        }
        for(int i = 0; i < s.length() - 2; i++){
            if(s.charAt(i) == s.charAt(i+1) || s.charAt(i) == s.charAt(i+2) || s.charAt(i+1) == s.charAt(i+2)){
                return false;
            }
        }
        return true;
    }
}  // Correct solution

Explanation:
The task is to check if the string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

The given code is correct. It checks if the length of the string is at least 3 and then checks if every 3 consecutive letters are distinct. If any 3 consecutive letters are the same, it returns false. If it doesn't find any duplicate 3 consecutive letters, it returns true.

The time complexity of this solution is O(n), where n is the length of the string. This is because it iterates over the string once. The space complexity is O(1), as it uses a constant amount of space to store the indices and characters.  // Correct solution

Explanation:
The task is to check if the string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

The given code is correct. It checks if the length of the string is at least 3 and then checks if every 3 consecutive letters are distinct. If any 3 consecutive letters are the same, it returns false. If it doesn't find any duplicate 3 consecutive letters, it returns true.

The time complexity of this solution is O(n), where n is the length of the string. This is because it iterates over the string once. The space complexity is O(1), as it uses a constant amount of space to store the indices and characters.  // Correct solution

Explanation:
The task is to check if the string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

The given code is correct. It checks if the length of the string is at least 3 and then checks if every 3 consecutive letters are distinct. If any 3 consecutive letters are the same, it returns false. If it doesn't find any duplicate 3 consecutive letters, it returns true.

The time complexity of this solution is O(n), where n