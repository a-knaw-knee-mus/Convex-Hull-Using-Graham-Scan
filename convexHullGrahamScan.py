import math
import matplotlib.pyplot as plt


def sort(array):
    start_point = array[0]

    for point in array:  # finds the point with the smallest y-val, if 2 point share it, one with smallest x is taken
        if point[1] < start_point[1]:
            start_point = point
        elif point[1] == start_point[1]:
            if point[0] < start_point[0]:
                start_point = point

    i = 0
    for point in array:  # remove the smallest point from list
        if point == start_point:
            array.pop(i)
        i += 1

    angle = []
    for point in array:
        angle.append(math.atan2(point[1] - start_point[1], point[0] - start_point[0]))

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
        point3 = array[i + 1]

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
        point3 = hull[j + 1]

        turn = (point2[0] - point1[0]) * (point3[1] - point1[1]) - (point2[1] - point1[1]) * (point3[0] - point1[0])
        if turn < 0:  # right turn
            return create_hull(hull)  # send the array with the unwanted points back into the function to weed them out
        j += 1
    return hull


def find_perimeter(array):
    i = 1
    prmtr = 0
    for point in array:
        point1 = point
        if i == len(array):
            point2 = array[0]
        else:
            point2 = array[i]
        prmtr += math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
        i += 1
    return prmtr


def find_area(array):
    array.append(array[0])
    i = 1
    det = 0
    for point in array:
        if i == len(array):
            break
        det += array[i][1]*point[0] - point[1]*array[i][0]  # area calculation using shoelace formula
        i += 1
    return 0.5*det


def plot(input_list, convex_hull, perm, total_area):
    font = {'family': 'sans-serif',
            'size': 8}

    # plot all the points
    x = []
    y = []
    x.append(convex_hull[0][0])
    y.append(convex_hull[0][1])
    for points in input_list:
        x.append(points[0])
        y.append(points[1])
    plt.plot(x, y, 'ok')

    # create the outer perimeter
    i = 1
    x_hull = []
    y_hull = []
    for points in convex_hull:
        x_hull.append(points[0])
        y_hull.append(points[1])
        if i == len(convex_hull):
            x_hull.append(convex_hull[0][0])
            y_hull.append(convex_hull[0][1])
        else:
            x_hull.append(convex_hull[i][0])
            y_hull.append(convex_hull[i][1])
        plt.plot(x_hull, y_hull, 'b')
        for i_x, i_y in zip(x_hull, y_hull):  # display the coordinates of the perimeter points
            plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y), font)
        x_hull.clear()
        y_hull.clear()
        i += 1

    plt.title('Convex Hull\n Perimeter of %.2f units\n Area of %.1f units^2' % (perm, total_area))
    plt.show()


file = open("data.txt", "r")
f = file.readlines()
inputList = []
for line in f:
    row = list(map(int, line.split()))
    inputList.append(row)

sortedList = sort(inputList)  # the list is now sorted in terms of CCW angle with reference point
convexHull = create_hull(sortedList)
print("THE POINTS THAT MAKE THE CONVEX HULL:\n" + str(convexHull))
perimeter = find_perimeter(convexHull)
print("\nThe perimeter in units is: %.2f" % perimeter)
area = find_area(convexHull)
print("The area in units^2 is:    %.1f" % area)
plot(sortedList, convexHull, perimeter, area)  # visually plot the points
