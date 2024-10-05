    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < message.length(); i++) {
        char c = message.charAt(i);
        if (c >= 'a' && c <= 'z') {
            sb.append((char)(c - 'a' + 'A'));
        } else if (c >= 'A' && c <= 'Z') {
            sb.append((char)(c - 'A' + 'a'));
        } else {
            int vowelIndex = "aeiou".indexOf(c);
            if (vowelIndex < 0) {
                sb.append(c);
            } else {
                char nextVowel = (char)(vowelIndex + 2);
                sb.append(nextVowel);
            }
        }
    }

    return sb.toString();

    }
}



# Python
def encode(message):
    sb = ""

    for c in message:
        if c.islower():
            sb += c.upper()
        elif c.isupper():
            sb += c.lower()
        else:
            vowelIndex = "aeiou".find(c)
            if vowelIndex < 0:
                sb += c
            else:
                nextVowel = chr(vowelIndex + 2)
                sb += nextVowel

    return sb


#!/usr/bin/env python

def encode(message):
    sb = ""

    for c in message:
        if c.islower():
            sb += c.upper()
        elif c.isupper():
            sb += c.lower()
        else:
            vowelIndex = "aeiou".find(c)
            if vowelIndex < 0:
                sb += c
            else:
                nextVowel = chr(vowelIndex + 2)
                sb += nextVowel

    return sb


#!/usr/bin/env python

from __future__ import division, print_function

import os
import sys
from io