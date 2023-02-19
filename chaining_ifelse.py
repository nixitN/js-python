def test_size(number):
    if number < 5:
        print("Tiny")
    elif number < 10:
        print("Small")
    elif number < 15:
        print("Medium")
    elif number < 20:
        print("Large")
    else:
        print("Huge")

test_size(7)