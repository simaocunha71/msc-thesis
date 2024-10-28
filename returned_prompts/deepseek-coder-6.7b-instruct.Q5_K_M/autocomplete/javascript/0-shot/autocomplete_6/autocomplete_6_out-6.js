
      if(token === tokens2[j])  {
        values += token + ' ';
        continue outer;
      }
    }
  }
  return values.trim();
}

'''

def token_difference(str1, str2):
    values = ''
    tokens1 = str1.split()
    tokens2 = str2.split()

    for i in range(len(tokens1)):
        token = tokens1[i]
        for j in range(len(tokens2)):
            if token == tokens2[j]:
                values += token + ' '
                break
    return values.strip()

#test_token_difference.py
import pytest
from token_difference import token_difference

def test_token_difference():
    assert token_difference("I love dogs", "I love cats") == "I love"
    assert token_difference("I love cats", "I love dogs") == "I love"
    assert token_difference("I love", "I love") == "I love"
    assert token_difference("", "") == ""
    assert token_difference("I love", "") == ""
    assert token_difference("I love", "I") == "I"
    assert token_difference("I love", "love I") == "love"
    assert token_difference("I love dogs", "I love") == "I love"
    assert token_difference("I love", "I love dogs") == "I love"
    assert token_difference("I love dogs", "I love dogs") == "I love dogs"
    assert token_difference("I love dogs and cats", "I love dogs") == "I love dogs"
    assert token_difference("I love dogs", "I love dogs and cats") == "I love dogs"
    assert token_difference("I love dogs and cats", "I love cats") == "I love cats"
    assert token_difference("I love cats", "I love dogs and cats") == "I love cats"
    assert token_difference("I love dogs and cats", "I love dogs and cats") == "I love dogs and cats