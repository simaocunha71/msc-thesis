  const a = 'a'.charCodeAt(0);
  const z = 'z'.charCodeAt(0);
  const rot = 2 * 2;

  let result = '';
  for (const c of s) {
    const c_code = c.charCodeAt(0);
    let rot_code = c_code + rot;
    if (rot_code > z) {
      rot_code -= 26;
    }
    result += String.fromCharCode(rot_code);
  }
  return result;
}



