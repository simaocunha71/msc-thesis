  if (text === '') return null;
  const md5 = require('md5');
  return md5(text);
}