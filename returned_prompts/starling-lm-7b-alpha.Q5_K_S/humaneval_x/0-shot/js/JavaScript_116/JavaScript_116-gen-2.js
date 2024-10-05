  const binary = (num) => {
    return (num >>> 0).toString(2);
  };

  return arr.sort((a, b) => {
    const aBinary = binary(a);
    const bBinary = binary(b);

    if (aBinary.length !== bBinary.length) {
      return aBinary.length - bBinary.length;
    }

    return aBinary > bBinary ? 1 : -1;
  });
};

*/

