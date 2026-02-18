A = [1,2,3,4,5]
B = [10,20,30,40]

print("union:", list(set(A) | set(B)))
print("intersection:", list(set(A) & set(B)))
print("difference:", list(set(A) - set(B)))