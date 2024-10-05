  if (txt.includes(" ")) {
    return txt.split(" ");
  } else if (txt.includes(",")) {
    return txt.split(",");
  } else {
    return txt.split("").filter(c => c == c.toLowerCase() && c != " ").length % 2;
  }
}