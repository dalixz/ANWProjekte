from EightBitAdder import EightBitAdder

for x in reversed(range(0, 8)):
    binary_a = [False, False, False, False, False, False, False, False]
    binary_a[x] = True

    for y in reversed(range(0, 8)):
        binary_b = [False, False, False, False, False, False, False, False]
        binary_b[y] = True

        eba = EightBitAdder()
        eba.set_input_binary(binary_a, binary_b)
        eba.execute()

        print("--------------------")
        print("Binary A: " + str(binary_a))
        print("Binary B: " + str(binary_b))
        print("Result Binary: " + str(eba.get_output_binary()))
        print("Result Carry: " + str(eba.get_output_carry()))
