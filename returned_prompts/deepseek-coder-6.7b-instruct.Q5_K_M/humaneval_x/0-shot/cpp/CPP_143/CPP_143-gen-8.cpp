    int i, j, flag;
    string word, new_sentence;
    stringstream ss(sentence);

B:
    while(!ss.eof()){
        flag = 0;
        ss >> word;

        if(word.length() <= 1){
            continue;
        }

        for(j = 2; j <= word.length()/2; j++){

            if(word.length() % j == 0){
                flag = 1;
                break;
            }
        }

        if(flag == 0){
            new_sentence += word + " ";
        }
    }

C:
    if(new_sentence.length() > 0){
        new_sentence.pop_back();
    }

D:
    return new_sentence;
}
*/
```

## Python Solution

```python
import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(" ")
    new_sentence = [word for word in words if is_prime(len(word))]
    return " ".join(new_sentence)

print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
```

## Explanation

In the Python solution, we first define a helper function `is_prime` that checks if a given number `n` is prime. It does this by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If it is, the function returns `False`; otherwise, it returns `True`.

Then, in the `words_in_sentence` function, we split the input sentence into a list of words. We then use a list comprehension to create a new list of words that have prime lengths. We do this by checking