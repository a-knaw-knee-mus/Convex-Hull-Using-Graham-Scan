from math import atan2
import matplotlib.pyplot as plt


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

    sorted_list = [z for _, z in sorted(zip(angle, array))]  # sort the list in terms of its angle
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

font = {'family': 'sans-serif',
        'size': 8}

x = []
y = []
for points in inputList:  # plot all the points
    x.append(points[0])
    y.append(points[1])
plt.plot(x, y, 'ok')

n = 1
x_hull = []
y_hull = []
for points in convexHull:
    x_hull.append(points[0])
    y_hull.append(points[1])
    if n == len(convexHull):
        x_hull.append(convexHull[0][0])
        y_hull.append(convexHull[0][1])
    else:
        x_hull.append(convexHull[n][0])
        y_hull.append(convexHull[n][1])
    plt.plot(x_hull, y_hull, 'b')
    for i_x, i_y in zip(x_hull, y_hull):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y), font)
    x_hull.clear()
    y_hull.clear()
    n += 1

plt.title('Convex Hull')
plt.show()
