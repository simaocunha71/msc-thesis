
  const checkType = (a) => {
    return (typeof a === "number") ? "number" : "string";
  }

  let typeA = checkType(a);
  let typeB = checkType(b);

  if(typeA === typeB){
    if(typeA === "number"){
      if(a > b) return a;
      else if(a < b) return b;
      else return null;
    } else {
      const splitA = a.split(",");
      const splitB = b.split(",");
      if(splitA[0] > splitB[0]) return a;
      else if(splitA[0] < splitB[0]) return b;
      else if(splitA[1] && splitB[1]) {
        if(splitA[1] > splitB[1]) return a;
        else if(splitA[1] < splitB[1]) return b;
        else return null;
      } else if(splitA[1]) {
        return a;
      } else {
        return b;
      }
    }
  } else {
    if(typeA === "number"){
      return b;
    } else {
      const splitA = a.split(",");
      const splitB = b.split(",");
      if(typeB === "number"){
        return a;
      } else {
        if(splitA[0] > splitB[0]) return a;
        else if(splitA[0] < splitB[0]) return b;
        else if(splitA[1] && splitB[1]) {
          if(splitA[1] > splitB[1]) return a;
          else if(splitA[1] < splitB[1]) return b;
          else return null;
        } else if(splitA[1]) {
          return a;
        } else {
          return b;
        }
      }
    }
  }
};

// Tests
console.log(compareOne(1, 2.5)); // 2.5
console.log(compareOne(1, "2,3")); // "2