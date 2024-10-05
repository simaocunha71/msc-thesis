  let count = (file_name.match(/[0-9]/g) || []).length;
  if (count > 3) return 'No';
  
  let split_name = file_name.split('.');
  if (split_name.length !== 2) return 'No';
  if (!split_name[0] || !split_name[1].match(/^[a-zA-Z]+$/)) return 'No';
  
  if (!['txt', 'exe', 'dll'].includes(split_name[1])) return 'No';
  
  return 'Yes';
}
fileNameCheck("example.txt") 
fileNameCheck("1example.dll") 
fileNameCheck("example123.txt") 
fileNameCheck("example.exe")
fileNameCheck("example1234.dll") 
fileNameCheck("123example.txt") 
fileNameCheck(".txt") 
fileNameCheck("example..dll") 
fileNameCheck("example.123") 
fileNameCheck("example123.dll.txt") 
fileNameCheck("example.dll.txt") 
fileNameCheck("example.123.txt") 
fileNameCheck("example.1234.dll") 
fileNameCheck("123.txt") 
fileNameCheck(".exe") 
fileNameCheck("example..txt") 
fileNameCheck("example.txt.dll") 
fileNameCheck("example.txt.123") 
fileNameCheck("example.dll.123.txt") 
fileNameCheck("example.123.txt.dll") 
fileNameCheck("example.exe.txt") 
fileNameCheck("example.dll.exe") 
fileNameCheck("example.dll.123.exe") 
fileNameCheck("example.123.txt.exe") 
fileNameCheck("example.1234.dll.exe") 
fileNameCheck("123.exe") 
fileNameCheck(".dll") 
fileNameCheck("example..exe") 
fileNameCheck("example.exe