class utils:
    def reversed(self, num):
        num = int(float(num))
        num_str = str(num)
        num_order_of_mag = len(num_str)
        counter = num_order_of_mag-1
        reversed_num = 0
        for x in range(num_order_of_mag-1, -1, -1):
            reversed_num = reversed_num + int(num_str[x])*(10**counter)
            counter = counter - 1
        return reversed_num

    def formatter(self, num):
        num = int(float(num))
        order_of_mag_counter = 0
        max_found = False
        
        while not max_found:
            if num >= 2**order_of_mag_counter:
                order_of_mag_counter = order_of_mag_counter + 1
                continue
            else:
                max_found = True

        binary_num = 0
        temp_num = num

        for i in range(order_of_mag_counter-1, -1, -1):
            if temp_num-2**i >= 0:
                binary_num = binary_num + 10**i 
                temp_num = temp_num -2**i

        temp_num = num
        octal_num = 0 
        magnitude_counter = 0

        while temp_num > 0:
            remainder = temp_num % 8
            temp_num = int(temp_num / 8)
            octal_num = octal_num + remainder * 10**magnitude_counter
            magnitude_counter = magnitude_counter + 1

        return binary_num, octal_num
