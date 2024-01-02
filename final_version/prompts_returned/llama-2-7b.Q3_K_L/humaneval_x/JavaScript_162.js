/*
  Given a string 'text', return its md5 hash equivalent string.
  If 'text' is an empty string, return null.

  >>> stringToMd5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
  */
const stringToMd5 = (text) => {
  if (!text || text.length === 0) return null;
  
  const map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'; // 36 characters is enough, because md5 hash of any string has length 32.
  
  let hash = '';
  for (let i = 0; i < text.length; i++) {
    const chr = text[i];
    
    if (map[chr] !== undefined) {
      hash += map[chr];
    } else {
      // do not include unmapped characters in the final hash
      return null;
    }
  }
  
  return hash;
};
