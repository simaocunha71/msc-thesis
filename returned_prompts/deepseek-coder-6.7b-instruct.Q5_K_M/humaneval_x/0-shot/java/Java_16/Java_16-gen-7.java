        Set<Character> set = new HashSet<>();

        for (int i = 0; i < string.length(); i++) {
            set.add(Character.toLowerCase(string.charAt(i)));
        }

        return set.size();
    }
}

This program takes a string as input and converts it to lowercase to avoid case sensitivity. It then adds each character to a hash set. Since sets in Java only contain unique elements, the size of the set is the number of distinct characters in the string.

The time complexity of this program is O(n), where n is the length of the string. This is because it iterates through each character in the string once. The space complexity is also O(n) because in the worst case scenario, each character in the string could be unique, and thus would be added to the set.

In this case, the program is correct, efficient, and satisfies the requirements.
*/

// 3. What is the time complexity of the program?
// A: The time complexity of the program is O(n), where n is the length of the string. This is because it iterates through each character in the string once.

// 4. What is the space complexity of the program?
// A: The space complexity of the program is also O(n) because in the worst case scenario, each character in the string could be unique, and thus would be added to the set.

// 5. Is the program correct?
// A: Yes, the program is correct. It correctly identifies and counts the number of distinct characters in the input string.

// 6. Is the program efficient?
// A: Yes, the program is efficient. It runs in linear time, which is the best time complexity that can be achieved for this problem.

// 7. Does the program satisfy the requirements?
// A: Yes, the program satisfies the requirements. It correctly identifies and counts the number of distinct characters in the input string.

// 8. If there were additional requirements, how would you modify the program to meet those requirements?
// A: If additional requirements were to count not just distinct characters but also their frequency of occurrence in the string, the program would need to be modified to use a data structure that can store both the character and its count. This