def mults(n):
    i = 1
    while True:
        yield i * n
        i += 1


primes = [601, 463, 41, 37, 29, 23, 19, 17, 13]

multiples = [mults(p) for p in primes]

delta = range(-primes[-1], primes[-1])

stop = False

i = 0

print("delta:", delta)

while not stop:
    stop = True
    i += 1
    pivot = next(multiples[0])
    # results = [(pivot, primes[0])]
    results = [pivot]
    print(f"pivot:", pivot)
    rng = range(pivot + delta.start, pivot + delta.stop)
    print("rng:", rng)
    for p, m in zip(primes[1:], multiples[1:]):
        item = next(m)
        print("p:", p, "item:", item)
        while item < rng.start:
            item = next(m)
            print("p:", p, "item:", item)
        if item not in rng:
            # goes to the end of the for
            stop = False
            break
        # results.append((item, p))
        # if item in results:
        #     stop = False
        #     break
        results.append(item)
        if rng.stop > item + p:
            print("adjust range", rng, item, item + p)
            rng = range(rng.start, item + p)
            if any(r not in rng for r in results):
                print("had item out")
                stop = False
                break
            else:
                print("AOK")

print("results:", sorted(results))


# results = [(56494, 601), (56486, 463), (56498, 41), (56499, 37), (56492, 29), (56488, 23), (56487, 19), (56491, 17), (56485, 13)]
# primes = [r[1] for r in results]

rng = range(min(results), max(results) + 1)
print("rng:", rng)
for n in rng:
    for p in primes:
        if n % p == 0:
            if not all(i % p != 0 for i in range(rng.start, n)):
                print(n, p, "bad")
                print([i % p for i in range(rng.start, n)])
            else:
                print(n, p, "good")

print("=" * 10)
print("=" * 10)
for i in rng:
    print(f"{i}:")
    for p in primes:
        if i % p == 0:
            print(f"    {p}: {i % p}")

print("=" * 10)

for p in primes:
    print(f"{p}:")
    for i in rng:
        if i % p == 0:
            print(f"    {i}")
