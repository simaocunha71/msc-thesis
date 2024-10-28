
return s.split("").map(ch => String.fromCharCode(
  ((ch.charCodeAt(0) - 5 + "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
)).join("");
};

Test.assertEquals(encodeShift("abc"), "fxu");
Test.assertEquals(decodeShift("fxu"), "abc");

/*
  returns true if the string is a valid Caesar cipher with shift n, otherwise false.
 */
const isValidCaesar = (s, n) => {
B:

return s.split("").every(ch => (ch.charCodeAt(0) - "a".charCodeAt(0) + n) % 26 === (String.fromCharCode(((ch.charCodeAt(0) - "a".charCodeAt(0) + n) % 26) + "a".charCodeAt(0)).charCodeAt(0) - "a".charCodeAt(0)))
};

Test.assertEquals(isValidCaesar("abc", 5), true);
Test.assertEquals(isValidCaesar("abc", 3), false);

/*
  returns the Caesar cipher decryption key, or -1 if the input is not a valid Caesar cipher.
 */
const caesarKey = (s) => {
C:

const key = Array.from(s).reduce((acc, ch) => {
  return (ch.charCodeAt(0) - "a".charCodeAt(0) + acc) % 26;
}, 0);

return isValidCaesar(s, key) ? key : -1;
};

Test.assertEquals(caesarKey("abc"), 5);
Test.assertEquals(caesarKey("xyz"), 5);
Test.assertEquals(caesarKey("abcdefghijklmnopqrstuvwxyz"), -1);

/*
  returns the Caesar cipher encryption key, or -1 if the input is not a valid Caesar cipher.
 */
const caesarShift = (s) => {
D:

return Array.from(s).reduce((acc, ch) => {
 