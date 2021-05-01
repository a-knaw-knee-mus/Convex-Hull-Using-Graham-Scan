from math import atan2


def sort(array):
    start_point = array[0]

    for point in array:  # finds the point with the smallest y-val, if 2 point share it, one with smallest x is taken
        if point[1] < start_point[1]:
            start_point = point
        elif point[1] == start_point[1]:
            if point[0] < start_point[0]:
                start_point = point

    count = 0
    for point in array:  # remove the smallest point from list
        if point == start_point:
            array.pop(count)
        count += 1

    angle = []
    for point in array:
        angle.append(atan2(point[1] - start_point[1], point[0] - start_point[0]))

    sorted_list = [x for _, x in sorted(zip(angle, array))]
    sorted_list.insert(0, start_point)
    return sorted_list


def create_hull(array):
    hull = []
    i = 1
    hull.append(array[0])
    for point in array:
        point1 = point
        point2 = array[i]
        point3 = array[i+1]

        turn = (point2[0] - point1[0]) * (point3[1] - point1[1]) - (point2[1] - point1[1]) * (point3[0] - point1[0])
        if turn >= 0:  # left turn
            hull.append(point2)
        if i == len(array) - 2:  # the point with the greatest angle which is always added
            hull.append(point3)
            break
        i += 1

    j = 1
    for point in hull:
        if j == len(hull) - 2:
            break
        point1 = point
        point2 = hull[j]
        point3 = hull[j+1]

        turn = (point2[0] - point1[0]) * (point3[1] - point1[1]) - (point2[1] - point1[1]) * (point3[0] - point1[0])
        if turn < 0:  # right turn
            return create_hull(hull)  # send the array with the unwanted points back into the function to weed them out
        j += 1
    return hull


file = open("data.txt", "r")
f = file.readlines()
inputList = []

for line in f:
    row = list(map(int, line.split()))
    inputList.append(row)

sortedList = sort(inputList)  # the list is now sorted in terms of CCW angle with reference point
convexHull = create_hull(sortedList)
print("THE POINTS THAT MAKE THE CONVEX HULL:\n" + str(convexHull))
