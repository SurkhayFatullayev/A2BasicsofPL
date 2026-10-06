#Set up sample number to convert to bytes and back
x = 0x12345678

#Show convertation to bytes using endianess
print("big-endian:")
print(x.to_bytes(4, byteorder="big").hex(),x.to_bytes(4, byteorder="big"))
print("little-endian:")
print(x.to_bytes(4, byteorder="little").hex(),x.to_bytes(4, byteorder="little"))
    
#Confirm that it is actually little endian
print("Confirming by big->big-endian: " + str(int.from_bytes(x.to_bytes(4, byteorder="big"), byteorder="big")))
print("Confirming by little->big-endian: " + str(int.from_bytes(x.to_bytes(4, byteorder="little"), byteorder="big")))

print("Confirming by big->little-endian: " + str(int.from_bytes(x.to_bytes(4, byteorder="big"), byteorder="little")))
print("Confirming by little->little-endian: " + str(int.from_bytes(x.to_bytes(4, byteorder="little"), byteorder="little")))


print("Hardware print(little-endian): " + str(x))