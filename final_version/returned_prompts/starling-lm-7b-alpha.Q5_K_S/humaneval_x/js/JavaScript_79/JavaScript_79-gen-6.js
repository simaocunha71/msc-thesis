  const result = [];
  for (let i = 0; decimal > 0; i++) {
    result.unshift(`${decimal & 1}`);
    decimal >>= 1;
  }
  return "db" + result.join("") + "db";
}



