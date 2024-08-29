  let ta = typeof(a)
  let tb = typeof(b)
  if (ta == "number" && tb == "number") {
    if (a == b) {
      return null
    } else if (a > b) {
      return a
    } else {
      return b
    }
  } else if (ta == "string" && tb == "string") {
    if (a == b) {
      return null
    } else if (a > b) {
      return a
    } else {
      return b
    }
  } else if (ta == "number" && tb == "string") {
    if (a == b) {
      return null
    } else if (a > b) {
      return a
    } else {
      return b
    }
  } else if (ta == "string" && tb == "number") {
    if (a == b) {
      return null
    } else if (a > b) {
      return a
    } else {
      return b
    }
  } else if (ta == "string") {
    return a
  } else if (tb == "string") {
    return b
  } else if (ta == "number") {
    return a
  } else if (tb == "number") {
    return b
  }
}



