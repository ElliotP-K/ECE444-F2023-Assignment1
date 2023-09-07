from utils import utils 

test_class = utils()

correct_test_count = 0

reversed_float = test_class.reversed(5.0)
if reversed_float == 5:
    correct_test_count = correct_test_count + 1
    print("reversed float works!")

reversed_int = test_class.reversed(5)
if reversed_float == 5:
    correct_test_count = correct_test_count + 1
    print("reversed int works!")

reversed_str = test_class.reversed('5.0')
if reversed_float == 5:
    correct_test_count = correct_test_count + 1
    print("reversed string works!")

binary_float, octal_float = test_class.formatter(10.0)
if binary_float == 1010:
    correct_test_count = correct_test_count + 1
    print("binary float works!")
if octal_float == 12:
    correct_test_count = correct_test_count + 1
    print("octal float works!")

binary_int, octal_int = test_class.formatter(10)
if binary_int == 1010:
    correct_test_count = correct_test_count + 1
    print("binary int works!")
if octal_int == 12:
    correct_test_count = correct_test_count + 1
    print("octal int works!")

binary_string, octal_string = test_class.formatter('10.0')
if binary_string == 1010:
    correct_test_count = correct_test_count + 1
    print("binary string works!")
if octal_string == 12:
    correct_test_count = correct_test_count + 1
    print("octal string works!")

if correct_test_count == 9:
    print("All tests pass")
