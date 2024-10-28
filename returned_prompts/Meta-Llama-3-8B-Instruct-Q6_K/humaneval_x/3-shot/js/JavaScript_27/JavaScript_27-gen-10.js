  return string.split('').map(c => c.toLowerCase() === c ? c.toUpperCase() : c.toLowerCase()).join('');
}
// Alternative solution:
// return string.replace(/([a-z])/g, function(match) { return match.toUpperCase(); }).replace(/([A-Z])/g, function(match) { return match.toLowerCase(); });
// Alternative solution:
// return string.split('').map(c => c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()).join('');
// Alternative solution:
// return string.split('').reduce((acc, curr) => acc + (curr === curr.toLowerCase() ? curr.toUpperCase() : curr.toLowerCase()), '');
// Alternative solution:
// return string.replace(/[a-z]/g, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[String.fromCharCode.toLowerCase().charCodeAt(0)]); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/[A-Z]/g, 'abcdefghijklmnopqrstuvwxyz'[String.fromCharCode.toUpperCase().charCodeAt(0)]); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/[a-z]/g, function(match) { return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[String.fromCharCode.toLowerCase().charCodeAt(0)].toLowerCase() }); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/[A-Z]/g, function(match) { return 'abcdefghijklmnopqrstuvwxyz'[String.fromCharCode.toUpperCase().charCodeAt(0)].toUpperCase() }); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/[a-z]/g, '1234567890'[String.fromCharCode.toLowerCase().charCodeAt(0)].toLowerCase()); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/[A-Z]/g, 'abcdefghijklmnopqrstuvwxyz'[String.fromCharCode.toUpperCase().charCodeAt(0)].toUpperCase()); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/([a-z])/g, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[String.fromCharCode.toLowerCase().charCodeAt(0)].toLowerCase()); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/([A-Z])/g, 'abcdefghijklmnopqrstuvwxyz'[String.fromCharCode.toUpperCase().charCodeAt(0)].toUpperCase()); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/[a-z]/g, function(match) { return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[String.fromCharCode.toLowerCase().charCodeAt(0)].toLowerCase() }); // This one is a bit tricky and not recommended
// Alternative solution:
// return string.replace(/[A-Z]/g, function