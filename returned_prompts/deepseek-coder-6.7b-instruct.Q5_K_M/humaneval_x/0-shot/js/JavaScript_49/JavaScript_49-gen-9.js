  return BigInt(2) ** BigInt(n) % BigInt(p)
}

console.log(modp(3, 5))
console.log(modp(1101, 101))
console.log(modp(0, 101))
console.log(modp(3, 11))
console.log(modp(100, 101))

