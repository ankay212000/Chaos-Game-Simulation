# Chaos-Game-Simulation
Interesting Outputs of Chaos Game


In mathematics, the term **Chaos game** originally referred to a method of creating a fractal, using a polygon and an initial point selected at random inside it. The fractal is created by iteratively creating a sequence of points, starting with the initial random point, in which each point in the sequence is a given fraction of the distance between the previous point and one of the vertices of the polygon; the vertex is chosen at random in each iteration. Repeating this iterative process a large number of times, selecting the vertex at random on each iteration, and throwing out the first few points in the sequence, will often (but not always) produce a fractal shape. Using a regular triangle and the factor 1/2 will result in the Sierpinski triangle, while creating the proper arrangement with four points and a factor 1/2 will create a display of a "Sierpinski Tetrahedron", the three-dimensional analogue of the Sierpinski triangle. As the number of points is increased to a number N, the arrangement forms a corresponding (N-1)-dimensional Sierpinski Simplex. 

## This Repository contains some interesting Fractals simulation in Python

- Sierpiński triangle

The Sierpiński triangle (sometimes spelled Sierpinski), also called the Sierpiński gasket or Sierpiński sieve, is a fractal attractive fixed set with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles. Originally constructed as a curve, this is one of the basic examples of self-similar sets—that is, it is a mathematically generated pattern that is reproducible at any magnification or reduction. It is named after the Polish mathematician Wacław Sierpiński, but appeared as a decorative pattern many centuries before the work of Sierpiński

<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Triangle.gif' alt = 'Me' align='center' height=300px width=600px/>

- Chaos game Square

If the chaos game is run with a square, no fractal appears and the interior of the square fills evenly with points. However, if restrictions are placed on the choice of vertices, fractals will appear in the square

<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Square.gif' alt = 'Me' align='center' height=300px width=600px/>

- Chaos Game Pentagon
 
When the jump is 1/2 and the point is jumping at random towards one or another of the five vertices of a regular pentagon, the chaos game generates a these fractals:

<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Pentagon.gif' alt = 'Me' align='center' height=300px width=600px/>

- Restricted Chaos Game

If restrictions are placed on the choice of vertices, we see different set of fractals
- Restricted Square 1

A point inside a square repeatedly jumps half of the distance towards a randomly chosen vertex, 
but the currently chosen vertex cannot be the same as the previously chosen vertex.  
 
<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Square%20Variation%201.gif' alt = 'Me' align='center' height=300px width=600px/>

- Restricted Square 2

A point inside a square repeatedly jumps half of the distance towards a randomly chosen vertex, but the currently chosen vertex cannot neighbor the previously chosen vertex if the two previously chosen vertices are the same.

<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Square%20Variation%202.gif' alt = 'Me' align='center' height=300px width=600px/>

- Restricted Pentagon 1

 A point inside a pentagon repeatedly jumps half of the distance towards a randomly chosen vertex, 
 but the currently chosen vertex cannot be the same as the previously chosen vertex.
 
<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Pentagon%20Variation%201.gif' alt = 'Me' align='center' height=300px width=600px/>

- Restricted Pentagon 2

A point inside a pentagon repeatedly jumps half of the distance towards a randomly chosen vertex, but the currently chosen vertex cannot neighbor the previously chosen vertex if the two previously chosen vertices are the same.

<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Pentagon%20Variation%202.gif' alt = 'Me' align='center' height=300px width=600px/>

![You can see more here](https://en.wikipedia.org/wiki/Chaos_game)

## Here is the interesting Part
- Generate Fern using Chaos Game

The fern is one of the basic examples of self-similar sets, i.e. it is a mathematically generated pattern that can be reproducible at any magnification or reduction. Like the Sierpinski triangle, the Barnsley fern shows how graphically beautiful structures can be built from repetitive uses of mathematical formulas with computers. Barnsley's 1988 book Fractals Everywhere is based on the course which he taught for undergraduate and graduate students in the School of Mathematics, Georgia Institute of Technology, called Fractal Geometry. After publishing the book, a second course was developed, called Fractal Measure Theory.[1] Barnsley's work has been a source of inspiration to graphic artists attempting to imitate nature with mathematical models. 

- Barnsley fern

<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Fern.gif' alt = 'Me' align='center' height=300px width=600px/>

- Barnsley fern variation

<img src = 'https://github.com/ankay212000/Chaos-Theory-Simulation/blob/main/Fern%20Variation%202.gif' alt = 'Me' align='center' height=300px width=600px/>
