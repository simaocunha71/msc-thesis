  let result = text;

  result = result.replace(/\s+/g, "_");
  result = result.replace(/_+/g, "-");

  return result;
}



