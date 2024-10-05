  if (dict == {}) {
    return false;
  }

  var lowercase = true;
  var uppercase = true;

  for (const key in dict) {
    if (typeof key != "string") {
      return false;
    }
    if (key.toLowerCase() != key) {
      lowercase = false;
    }
    if (key.toUpperCase() != key) {
      uppercase = false;
    }
    if (!lowercase && !uppercase) {
      return false;
    }
  }

  return true;
}



