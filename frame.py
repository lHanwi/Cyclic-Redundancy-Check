class Frame:
    def __init__(self, destination_mac, source_mac, ether_type, payload, crc=None):
        self.header = destination_mac + source_mac + ether_type
        self.payload = payload
        self.crc = crc
        self.generator= "100000100110000010001110110110111"

    def hex_to_bin(self, hex_data):
        bit_stream = ""

        for char in hex_data:

            decimal_value = int(char, 16)

            binary_value = bin(decimal_value)[2:]

            while len(binary_value) < 4:
                binary_value = "0" + binary_value

            bit_stream += binary_value

        return bit_stream

    def bin_to_hex(self, bin_data):
        hex_stream = ""

        for i in range(0, len(bin_data), 4):

            four_bits = bin_data[i:i+4]

            decimal_value = int(four_bits, 2)

            hex_char = hex(decimal_value)[2:].upper()

            hex_stream += hex_char

        return hex_stream

    
    def XOR(self, bit_stream, generator):

        bit_stream = list(bit_stream)
        generator = list(generator)
            

        for i in range(len(bit_stream) - len(generator) + 1):

            if bit_stream[i] == "1":

                for j in range(len(generator)):

                    if bit_stream[i + j] == generator[j] :
                        bit_stream[i + j] = "0"
                    else:
                        bit_stream[i + j] = "1"
            
        remainder = "".join(bit_stream[-(len(generator) - 1):])
        return remainder
    

    def calculate_crc(self):
        data = self.hex_to_bin(self.header + self.payload)
        padded_data = data + ("0" * 32)
        crc = self.XOR(padded_data, self.generator)
        crc_hex = self.bin_to_hex(crc)

        transmitted_data = self.header + self.payload + crc_hex
        print(f"The CRC is : {crc_hex}")
        print(f"--> The transmitted data is: {transmitted_data}")


    def verify_crc(self):

        data = self.hex_to_bin(self.header + self.payload + self.crc)
        remainder = self.XOR(data, self.generator)
        print(f"The remainder is: {remainder}")
        if "1" not in remainder:
            print("--> The frame is valid.")
            return True
        else:
            print("--> The frame is corrupted!")



destination = "A1B2C3D4E5F6"
source = "1A2B3C4D5E6F"
ether_type = "0800"
payload = "505871AB"

frame = Frame(destination, source, ether_type, payload)
frame.calculate_crc()

print("----------------------------------------------------------")

received_frame = Frame(destination, source, ether_type, payload, crc="E935DDF1")
received_frame.verify_crc()
