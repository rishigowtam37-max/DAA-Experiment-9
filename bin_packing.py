items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
capacity = 1.0


def first_fit(items):
    bins = []

    for item in items:
        placed = False

        for b in bins:
            if sum(b) + item <= capacity:
                b.append(item)
                placed = True
                break

        if not placed:
            bins.append([item])

    return bins


def best_fit_decreasing(items):
    bins = []

    for item in sorted(items, reverse=True):
        best = -1
        space = capacity + 1

        for i in range(len(bins)):
            remaining = capacity - sum(bins[i])

            if item <= remaining and remaining < space:
                space = remaining
                best = i

        if best == -1:
            bins.append([item])
        else:
            bins[best].append(item)

    return bins


def print_result(name, bins):
    print(name)
    for i, b in enumerate(bins, 1):
        print("Bin", i, ":", b, "Total =", round(sum(b), 2))
    print("Number of bins:", len(bins))
    print()


# First Fit
ff = first_fit(items)

# First Fit Decreasing
ffd = first_fit(sorted(items, reverse=True))

# Best Fit Decreasing
bfd = best_fit_decreasing(items)

print_result("First Fit", ff)
print_result("First Fit Decreasing", ffd)
print_result("Best Fit Decreasing", bfd)

lower_bound = sum(items) / capacity

print("Theoretical Lower Bound:",
      int(lower_bound) if lower_bound.is_integer()
      else int(lower_bound) + 1)
