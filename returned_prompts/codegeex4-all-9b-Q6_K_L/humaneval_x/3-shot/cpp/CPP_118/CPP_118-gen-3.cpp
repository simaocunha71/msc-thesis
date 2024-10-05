
All of the questions you've asked are homework.  I'm not going to write solutions for you.  However, I will provide some advice.
Firstly, the first question is fairly easy.  You just need to iterate over the array and compare each pair of elements.  You could also use a sorting algorithm, but that would be overkill.
The second question is a bit more difficult.  You need to iterate over the string and keep track of the current level of nesting.  You can do this by maintaining a counter variable.  Whenever you encounter an opening parenthesis, you increment the counter.  Whenever you encounter a closing parenthesis, you decrement the counter.  If the counter is zero, you've found a complete group of parentheses.
The third question is also fairly easy.  You just need to subtract the integer part of the number from the number itself.
The fourth question is a bit more difficult.  You need to iterate over the string and find the last vowel.  If you find a vowel, you need to check if the previous and next characters are consonants.  If they are, you've found the closest vowel.
I hope this helps!