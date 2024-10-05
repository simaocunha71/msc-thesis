const flipCase = string => string.replace(/[a-z]/g, c => String.fromCharCode(c.charCodeAt(0) ^ 32))

