  var result = text.replace(/ /g, '_');
  result = result.replace(/_+/g, '-');
  return result;
}