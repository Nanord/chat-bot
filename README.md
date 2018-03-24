`def string_to_bit_array(text):#переводит строку в список бит
	array = list()
	for char in text:
	    binval = binvalue(char, 8)
	    array.extend([int(x) for x in list(binval)])
	return array

def bit_array_to_string(array): #Восстанавливает строку
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in bytes]) for bytes in  nsplit(array,8)]])   
    return res

def binvalue(val, bitsize): #Возвращает двоичное значение как строку заданного размера
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Добавляет 0, чтобы получить желаемый размер
    return binval`
