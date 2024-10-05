public class Main {
  public static void main(String[] args) {
    System.out.println(encrypt("hi")); // lm
    System.out.println(encrypt("asdfghjkl")); // ewhjklnop
    System.out.println(encrypt("gf")); // kj
    System.out.println(encrypt("et")); // ix
  }

  public static String encrypt(String s) {
    String encrypted = "";
    for (char c : s.toCharArray()) {
      if (Character.isLetter(c)) {
        char encryptedChar = (char) (c + 8);
        if (Character.isUpperCase(c) && encryptedChar > 'Z') {
          encryptedChar = (char) (encryptedChar - 26);
        } else if (Character.isLowerCase(c) && encryptedChar > 'z') {
          encryptedChar = (char) (encryptedChar - 26);
        }
        encrypted += encryptedChar;
      } else {
        encrypted += c;
      }
    }
    return encrypted;
  }
}