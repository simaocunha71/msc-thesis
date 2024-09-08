  if (Object.keys(dict).length === 0) {
    return true;
  }

  for (const key in dict) {
    if (typeof dict[key] === "string") {
      if (key === key.toLowerCase() || key === key.toUpperCase()) {
        continue;
      } else {
        return false;
      }
    } else {
      return false;
    }
  }

  return true;
}



