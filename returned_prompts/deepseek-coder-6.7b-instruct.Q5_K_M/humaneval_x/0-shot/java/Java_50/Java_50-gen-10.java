        StringBuilder sb = new StringBuilder();
        for  (char ch : s.toCharArray())  {
            sb.append((char)  ('a' + ((ch - 5 - 'a' + 26) % 26)));
        }
        return sb.toString();
    }
}


A: Here is the corrected code:
import java.util.*;
import java.lang.*;

class Solution  {
    /**
    returns encoded string by shifting every character by 5 in the alphabet.
      */
    public String encodeShift(String s)  {
        StringBuilder sb = new StringBuilder();
        for  (char ch : s.toCharArray())  {
            sb.append((char)  ('a' + ((ch - 'a' + 5) % 26)));
        }
        return sb.toString();
    }

    /**
    takes as input string encoded with encodeShift function. Returns decoded string.
      */
    public String decodeShift(String s)  {
        StringBuilder sb = new StringBuilder();
        for  (char ch : s.toCharArray())  {
            sb.append((char)  ('a' + ((ch - 'a' - 5 + 26) % 26)));
        }
        return sb.toString();
    }
}

Here, for encoding, I subtracted 5 from the ASCII value of the character and then modulo 26 it to keep it in the range of alphabets. For decoding, I added 5 to the ASCII value and then modulo 26 it to keep it in the range of alphabets. Also, I added 26 before subtraction to handle the negative case in modulo operation.

A: Your code has a typo in the decodeShift method. This line
sb.append((char)  ('a' + ((ch - 5 - 'a' + 26) % 26)));

should be
sb.append((char)  ('a' + ((ch - 'a' + 26 - 5) % 26)));

This is because you want to shift characters 5 positions to the left, so you subtract 5 from the