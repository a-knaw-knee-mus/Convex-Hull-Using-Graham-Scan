# Convex-Hull-Using-Graham-Scan
This is a Convex Hull created using Graham Scan in Python 3 using _recursion_.<br>
-Essentially, the code reads from a text file, a list of 2D coordinates.<br>
-It then picks the point with the smallest y-val. In the case of multiple points with the same y-val, it picks the one with the smallest x-val. This is the starting point.<br>
-Once the starting point has been selected, it orders the others points in order of the angle they make with the starting point and the x-axis.<br>
-The code then takes 3 consecutive points and determines if a left or right turn is made. If a left turn is made, it adds the second point to the hull.<br>
-This has the potential of adding unwanted points to the hull which is why recursion is used. This new array is then sent back into the function if a right turn is detected, indicating an unwanted point in the hull.<br>
-The recursion will continue to loop, sending the array back into the function until no right turn is detected. The convex hull is now complete.
## Upcoming Improvements
1) Calculate the perimeter
2) Visual representation of the points and the hull
3) Attempt to calculate the area enclosed
## Updates
1) Created a visual representation using matplotlib instead of pygame that also has the convex points on the plot
