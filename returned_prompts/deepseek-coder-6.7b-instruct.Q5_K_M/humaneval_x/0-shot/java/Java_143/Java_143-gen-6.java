        //Split the input string into words
        String[] words = sentence.split(" ");

        //Create a string builder to build the output string
        StringBuilder sb = new StringBuilder();

        //Iterate over the words
        for(String word : words) {
            //Check if the length of the word is a prime number
            if(isPrime(word.length())) {
                //If yes, append it to the output string
                sb.append(word).append(" ");
            }
        }

        //Return the output string without the trailing space
        return sb.toString().trim();
    }

    //Helper function to check if a number is a prime number
    private static boolean isPrime(int num) {
        if(num <= 1) {
            return false;
        }
        for(int i = 2; i * i <= num; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }

}


A: Here is the solution for the problem statement.

I have created a function called wordsInSentence that takes a string sentence as an input.

In this function, I have first used split function of java to split the given sentence into words.

Then, I have created a StringBuilder object sb to store the words whose lengths are prime numbers.

After that, I have iterated over the words and for each word, I have checked whether the length of the word is a prime number or not.

If the length of the word is a prime number, I have appended the word to the StringBuilder object sb.

Finally, I have returned the string representation of the StringBuilder object sb without the trailing space using the trim function.

In the end, I have also created a helper function isPrime which checks whether a number is a prime number or not.

This helper function takes an integer num as input and returns a boolean value indicating whether num is a prime number or not.

In the isPrime function, I have first checked whether num is less than or equal to 1. If yes, I have returned false as a prime number is a positive integer greater than 1.

Then, I have iterated from 2