synthetic_index = float(input())

if synthetic_index < 2:
    print("Analytic")
elif synthetic_index >= 2 and synthetic_index <= 3:
    print("Synthetic")
elif synthetic_index > 3:
    print("Polysynthetic")
