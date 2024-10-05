const sameChars = (s0, s1) => {
  const [s0Arr, s1Arr] = [s0.split(""), s1.split("")];
  return s0Arr.every((c, i) => c === s1Arr[i]);
};
