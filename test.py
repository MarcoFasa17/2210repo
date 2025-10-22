def tables():
    for i in range(1, 11):
        print(f"Multiplication table for {i}")   # ← indented
        print("-" * 25)
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print()

tables()
print("hello")
print("this is Jenkins class")
print("bye")