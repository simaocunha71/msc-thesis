  if (txt.search(/\s+/) == -1) {
    return txt.split(',');
  } else {
    return txt.split(/\s+/);
  }
}



