def encode(c):
    ls=10
    rs=2
    mul=3
    ad=125
    return (~(c<<ls|c>>rs))&((c*mul)|(c+ad))
ans=[]
flag=[205, 486, 483, 484, 486, 481, 236, 483, 485, 486, 480, 480, 486, 484]
inp=input("Enter the flag\n")
for i in inp:
    ans.append(encode(ord(i)))
if ans==flag:
    print("Congrats! You found the flag")
else:
    print("Flag Incorrect")
