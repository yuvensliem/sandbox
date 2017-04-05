"""
Yuvens Enverd Liem
Add error checking
sadjiasdjaisd
"""
def main():
    get_name()


def get_name():
    name = str(input("Please enter your name :"))
    x = len(name)
    while x == 0:
        name = str(input("Please enter your name :"))
    for i in range (0, x, 2):
        print(name[i])


main()
"""
asudhausdh
"""