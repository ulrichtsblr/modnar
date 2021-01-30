def lcg(x, a, c, m):
    x = (a * x + c) % m
    return x
def generate_bsdrand(n, seed):
    a, c, m = 1103515245, 12345, 2 ** 31
    sample = []
    for _ in range(n):
        seed = lcg(seed, a, c, m)
        sample.append(seed)
    return sample
def print_bsdrand(sample):
    for _ in sample:
        print("<{}>".format(_))
def main():
    message = "linear congruential generator"
    n = 32
    seed = 0
    if n > 0 and n <= 32:
        print(message)
        sample = generate_bsdrand(n, seed)
        print_bsdrand(sample)
    else:
        print("console overflow")
main()
