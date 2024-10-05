
const encode = (message) => {
  let newMessage = ''
  for (let i = 0; i < message.length; i++){
    if (message[i].match(/[A-Z]/)){
      newMessage += message[i].toLowerCase()
    } else {
      newMessage += message[i].toUpperCase()
    }
  }
  return newMessage
}

B:

const encode = (message) => {
  let newMessage = ''
  for (let i = 0; i < message.length; i++){
    if (message[i].match(/[a-z]/)){
      let charCode = message[i].charCodeAt(0) + 2
      if (charCode > 90) {
        charCode = charCode - 26
      }
      newMessage += String.fromCharCode(charCode)
    } else {
      newMessage += message[i]
    }
  }
  return newMessage
}

C:

const encode = (message) => {
  let newMessage = ''
  for (let i = 0; i < message.length; i++){
    if (message[i].match(/[a-z]/)){
      let charCode = message[i].charCodeAt(0) + 2
      if (charCode > 90) {
        charCode = charCode - 26
      }
      newMessage += String.fromCharCode(charCode)
    } else {
      newMessage += message[i]
    }
  }
  return newMessage
}
