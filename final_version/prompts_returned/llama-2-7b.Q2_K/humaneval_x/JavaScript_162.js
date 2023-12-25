/*
  Given a string 'text', return its md5 hash equivalent string.
  If 'text' is an empty string, return null.

  >>> stringToMd5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
  */
const stringToMd5 = (text) => {
  if (!text || text.length === 0) return null;
  // const hexDigits = '0123456789abcdef';
  let md5hex = '';
  for (let i = 0, l = text.length; i < l; ++i) {
    md5hex += text.charCodeAt(i).toString(16);
  }
  return md5hex;
};

module.exports = stringToMd5;