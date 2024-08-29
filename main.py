# 📍Task: Write a Python program to calculate the Euclidean distance between all pairs of points and find the minimum distance.

import math

points = [(3, 4), (0, 0), (5, 9), (1, 2), (8, 6)]   # points definition
distances = []     # store distances

# Calculates the Euclidean distance between two points
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Calculates the distances between all pairs of points
def calculate_dist():
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclideanDistance(points[i], points[j])
            distances.append(dist)

# Find and print min distance
def find_min():
    min_distance = min(distances)
    print("Min Distance:", min_distance)

# Main function
if __name__ == '__main__':
    calculate_dist()
    find_min()