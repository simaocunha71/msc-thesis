    StringBuilder result = new StringBuilder();

    for (char c : message.toCharArray()) {
      if (c >= 'a' && c <= 'z') {
        result.append((char) (c - 'a' + 'A'));
      } else if (c >= 'A' && c <= 'Z') {
        result.append((char) (c - 'A' + 'a'));
      } else if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        result.append((char) (c + 2));
      } else {
        result.append(c);
      }
    }

    return result.toString();

    }
}


Answer:
Solution:
public String encode(String message) {

    StringBuilder result = new StringBuilder();

    for (char c : message.toCharArray()) {
      if (c >= 'a' && c <= 'z') {
        result.append((char) (c - 'a' + 'A'));
      } else if (c >= 'A' && c <= 'Z') {
        result.append((char) (c - 'A' + 'a'));
      } else if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        result.append((char) (c + 2));
      } else {
        result.append(c);
      }
    }

    return result.toString();

    }














































































































































