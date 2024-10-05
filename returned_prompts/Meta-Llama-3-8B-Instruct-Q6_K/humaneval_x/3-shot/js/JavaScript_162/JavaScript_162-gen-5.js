  if (text === "") {
    return null;
  }

  const crypto = require("crypto");
  const md5 = crypto.createHash("md5");
  const hash = md5.update(text).digest("hex");

  return hash;
}