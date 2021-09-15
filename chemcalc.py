A = float(input("Enter A Value: "))
B = float(input("Enter B Value: "))
per_A = float(input("Enter Percent A Value in Decimal Form: "))
per_B = float(input("Enter Percent B Value in Decimal Form: "))
amt = float(input("Enter Amount of Iterations: "))

i = 0
while i < amt:
    sub_A = A * per_A
    A = A - sub_A

    sub_B = B * per_B
    B = B - sub_B

    A = A + sub_B
    B = B + sub_A
    print("========================")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"Index:{i+1}")
    i += 1

print("========================")
print(f"Your equilibrium end values are, A:{A} B:{B}")
print()

A_simp = round(A, 2)
B_simp = round(B, 2)

print(f"Your simplified values are, A: {A_simp} B: {B_simp}")
print()
print(f"Simplified form: {round(A_simp/A_simp,2)} : {round(B_simp/A_simp,2)}")

#Initial functional commit, another branch in development.
