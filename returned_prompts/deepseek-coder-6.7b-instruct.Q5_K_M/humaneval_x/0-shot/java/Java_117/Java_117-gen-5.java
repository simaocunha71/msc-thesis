        List<String> list = new ArrayList<String>();
        String[] words = s.split(" ");
        for(String word: words){
            int consonantCount = 0;
            for(char c: word.toCharArray()){
                if(!"aeiouAEIOU ".contains(Character.toString(c))){
                    consonantCount++;
                }
            }
            if(consonantCount == n){
                list.add(word);
            }
        }
        return list;
    }
}

This solution works by splitting the input string into words and then checking each word to see if it contains exactly n consonants. If it does, it adds that word to the list. The function then returns this list. 

The time complexity of this solution is O(n*m), where n is the number of words in the string and m is the length of the longest word.
The space complexity is also O(n*m), as we are storing the words in a list.

The "Character.toString(c)" is used to convert the character c to a string, because the "contains" method in Java works on strings, not characters.

The "!" operator in Java is a logical NOT operator. It inverts the boolean value of its operand.

The "contains" method in Java checks if a specific element is present in a collection or not. In this case, it is used to check if a character is a vowel or not.

The "split" method in Java is used to split a string into an array of strings. In this case, it is used to split the string into words.

The "toCharArray" method in Java is used to convert a string into an array of characters.

The "ArrayList" class in Java is used to create a list (an ordered collection) of objects. In this case, we are using it to store the words that contain exactly n consonants.

The "add" method in Java is used to add an element to the end of the list.

The "return" keyword is used to return the list of words that contain exactly n consonants.

This solution assumes that the input string only contains letters and spaces, as per the problem statement. If it contains any other characters, the solution may