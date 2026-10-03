def hanoi(n, A, B, C, nameA, nameB, nameC):
    if n == 1:
        disk = A.pop()
        C.append(disk)

        print(f"Move disk {disk}: {nameA} -> {nameC}")
        print(A, B, C)
        print()

        return

    # Move n-1 disks from A to B
    hanoi(n - 1, A, C, B, nameA, nameC, nameB)

    # Move the largest disk from A to C
    disk = A.pop()
    C.append(disk)

    print(f"Move disk {disk}: {nameA} -> {nameC}")
    print(A, B, C)
    print()

    # Move n-1 disks from B to C
    hanoi(n - 1, B, A, C, nameB, nameA, nameC)


n = 5

A = list(range(n, 0, -1))
B = []
C = []

print("Initial:")
print(A, B, C)
print()

hanoi(n, A, B, C, "A", "B", "C")

print("Final:")
print(A, B, C)


def tower_of_hanoi(disks, source, auxiliary, destination):
    if disks == 1: 
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(disks - 1, source, destination, auxiliary)
    print(f"Move disk {disks} from {source} to {destination}") 
    tower_of_hanoi(disks - 1, auxiliary, source, destination)

tower_of_hanoi(4, "A", "B", "C")