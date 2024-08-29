  if (typeof a === "number" && typeof b === "number") {
    return a > b ? a : b === a ? null : b;
  } else if (typeof a === "string" && typeof b === "number") {
    let a_parts = a.split(".");
    return Number(a_parts[0] + "." + a_parts[1].substring(0, 1)) > b ?
      a : b === Number(a_parts[0] + "." + a_parts[1].substring(0, 1)) ? null : b;
  } else if (typeof a === "number" && typeof b === "string") {
    return a > b ? a : b === a ? null : a;
  } else if (typeof a === "string" && typeof b === "string") {
    let a_parts = a.split(".");
    let b_parts = b.split(".");
    return a_parts[0] + "." + a_parts[1].substring(0, 1) > b_parts[0] + "." + b_parts[1].substring(0, 1) ?
      a : b === (a_parts[0] + "." + a_parts[1].substring(0, 1)) ? null : b;
  }
}



