        StringBuilder encodedMsg = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    encodedMsg.append(Character.toUpperCase(c));
                } else {
                    encodedMsg.append(Character.toLowerCase(c));
                }
            } else {
                encodedMsg.append(c);
            }
        }

        return encodedMsg.toString();
    }
}


A: Your question asks for a function that takes a string and swaps the case of all letters, but it doesn't specify what to do with non-letter characters or with vowels. 
As per the problem statement, it suggests that vowels should be replaced by the letter that appears 2 places ahead in the alphabet. 
For this, you can use the following code:

```java
public String encode(String message) {
    StringBuilder encodedMsg = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            if (Character.isLowerCase(c)) {
                switch(c){
                    case 'a': encodedMsg.append('c'); break;
                    case 'e': encodedMsg.append('g'); break;
                    case 'i': encodedMsg.append('k'); break;
                    case 'o': encodedMsg.append('q'); break;
                    case 'u': encodedMsg.append('w'); break;
                    default : encodedMsg.append(Character.toUpperCase(c));
                }
            } else {
                switch(Character.toLowerCase(c)){
                    case 'a': encodedMsg.append('C'); break;
                    case 'e': encodedMsg.append('G'); break;
                    case 'i': encodedMsg.append('K'); break;
                    case 'o': encodedMsg.append('Q'); break;
                    case 'u': encodedMsg.append('W'); break;
                    default : encodedMsg.append(Character.toLowerCase(c));
                }
            }
        } else {
            encodedMsg.append(c);
        }
    }
    return