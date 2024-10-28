  if (txt.includes(" ") || txt.includes(",")) {
    return txt.split(/\s+/);
  } else {
    return txt.split(",").length;
  }
}



