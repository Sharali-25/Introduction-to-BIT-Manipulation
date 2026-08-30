secret_code = 15
access_key = 9
def bits(number, width = 3):
    return format (number & 1 ((1<< width) - 1 ) f"0{width}b"):
print("MY SECRET CODE BIT SCANNER")
print("secret code ",secret_code, "Binary ",bits(secret_code))
print("Acess key ", access_key,"Binary ",bits(access_key))

print("Binary numbers only use 0 and 1 .")
print(" Secret Binary code = ",bits(secret_code))
print("Access Key Binary = ", bits(access_key))

and_result = secret_code& access_key
or_result = secret_code | access_key
print("AND result : ",and_result,"Binary : ", bits(and_result))
print(" OR results : ",or_result,"Binary: ",bits(or_result))


not_result = secret_code & 0b1111
xor_result = secret_code ^ access_key
print("NOT secret code result within 4 bits", not_result,"Binary ", bits(not_result))
print("XOR result ", xor_result,"Binary",bits(xor_result))



