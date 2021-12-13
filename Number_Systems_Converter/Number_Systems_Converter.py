# Function that converts Binary values to Denary
def Binary_To_Denary(Binary_value1):
    Binary_value1 = Binary_value1.replace(" ", "")
    Denary_value1 = 0
    Number1 = 1
    for i in range(len(Binary_value1)):
        Denary_value1 += int(Binary_value1[-(i+1)]) * Number1
        Number1 *=2
    return str(Denary_value1)

# Function that converts Denary to Binary
def Denary_to_Binary(Denary_value2):
    Denary_value2 = Denary_value2.replace(" ", "")
    Denary_value2 = int(Denary_value2)
    Place_values2 = [128, 64, 32, 16, 8, 4, 2, 1]
    Binary_value2 = ""
    for i in range(len(Place_values2)):
        if Denary_value2 >= Place_values2[i]:
            Denary_value2 -= Place_values2[i]
            Binary_value2 +="1"
        else:
            Binary_value2 +="0"
    return Binary_value2

Convert_from = input("Number system to convert from: ").lower().replace(" ", "")
Convert_to = input("Number system to convert to: ").lower().replace(" ", "")
Value = input("Value: ")
if Convert_from == "binary" and Convert_to == "binary":
    print("Value in " + Convert_to.capitalize() + ": " + Value)
elif Convert_from == "binary" and Convert_to == "denary":
    print("Value in " + Convert_to.capitalize() + ": " + Binary_To_Denary(Value))
elif Convert_from == "denary" and Convert_to == "binary":
    print("Value in " + Convert_to.capitalize() + ": " + Denary_to_Binary(Value))
elif Convert_from == "denary" and Convert_to == "denary":
    print("Value in " + Convert_to.capitalize() + ": " + Value)
else:
    print("""
    Number system does not exist or has not been added to program.
    Only Binary or Denary conversion is supported right now.
    """)
