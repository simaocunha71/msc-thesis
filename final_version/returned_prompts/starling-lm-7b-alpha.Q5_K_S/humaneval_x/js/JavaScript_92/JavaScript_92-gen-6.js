  return (typeof x === "number" && typeof y === "number" && typeof z === "number" &&
    Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) &&
    (x === y + z || y === x + z || z === x + y);
}



