import numpy as np


def Exponential(lam):
    U = np.random.uniform(0, 1)
    return -(1 / lam) * np.log(U)

def generate_events(rate, time_limit):
    t = 0
    times = []
    while t < time_limit:
        t += Exponential(rate)
        if t < time_limit:
            times.append(t)
    return times


time = 24*60
arrival_rate = 0.2
leaving_rate = 0.17
spaces = [0] * 75


arrivals = generate_events(arrival_rate, time)
leavings = generate_events(leaving_rate, time)


Leaving_index = 0

for current in arrivals:
    while Leaving_index < len(leavings) and leavings[Leaving_index] <= current:
        occupied = [i for i, x in enumerate(spaces) if x == 1]
        if occupied:
            spot = np.random.choice(occupied)
            spaces[spot] = 0
        Leaving_index += 1


    Y = np.random.randint(0, len(spaces))
    if spaces[Y] == 0:
        spaces[Y] = 1
    else:
        n = len(spaces)
        for d in range(1, n):
            left = Y - d
            right = Y + d
            if left >= 0 and spaces[left] == 0:
                spaces[left] = 1
                break
            elif right < n and spaces[right] == 0:
                spaces[right] = 1
                break

print("Final occupancy:", sum(spaces), "/", len(spaces))
print("Spaces (1 = occupied, 0 = empty):")
print(spaces)

