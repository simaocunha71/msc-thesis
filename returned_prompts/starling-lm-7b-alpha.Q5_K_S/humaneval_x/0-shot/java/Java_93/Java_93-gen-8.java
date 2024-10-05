    String result = "";
    for (char c : message.toCharArray()) {
      if (c >= 'a' && c <= 'z') {
        result += (char) (c - 32);
      } else if (c >= 'A' && c <= 'Z') {
        result += (char) (c + 32);
      } else if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        result += (char) (((c - 'a' + 2) % 26) + 'a');
      }
    }
    return result;
  }
}



# Python

def encode(message):
    result = ""
    for char in message:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        elif char in "aeiou":
            result += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
    return result


# Python

def encode(message):
    result = ""
    for char in message:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        elif char in "aeiou":
            result += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
    return result


# Python

def encode(message):
    result = ""
    for char in message:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        elif char in "aeiou":
            result += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
    return result


# Python

def encode(message):
    result = ""
    for char in message:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
       