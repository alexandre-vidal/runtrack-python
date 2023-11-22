x = "abcdefghijklmnopqrstuvwxyz"

for y in range(1, len(x)):
    subset = x[:y*2-1]
    repeated_subset = (subset * 2)[:y*2-1]
    print(repeated_subset)