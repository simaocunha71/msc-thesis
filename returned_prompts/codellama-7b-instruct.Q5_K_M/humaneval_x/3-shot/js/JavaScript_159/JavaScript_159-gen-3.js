  var eaten = number + need;
  if (eaten <= remaining) {
    return [eaten, remaining - eaten];
  } else {
    return [remaining, 0];
  }
}



