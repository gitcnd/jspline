# jspline

Multi-dimensional parameterized spline curves (snappiness parameter gives uniform cubic B-splines, four-point subdivision splines, uniform quintic B-splines, and everything in-between)

# Description
    
J-Splines are awesome: they're a class of spline curves that take a shape parameter, s. Setting s=1 yields uniform cubic B-spline curves, s=0 gives four-point subdivision curves, s=0.5 are uniform quintic B-splines - and more. "s" basically governs the "snappiness" of the curve.

`jspline`, lets you choose any combination of J-Spline parameters for any number of input arrays, with a range of different starting and ending schemes (eg: open or closed loops). Use it for 2D drawing, 3D graphics, or any other kind of interpolation you might need.

- See also my CPAN perl module that does the same: https://metacpan.org/pod/Math::JSpline

# Synopsis

```python
from jspline import jspline
interpolated_results=jspline.make(subdivision_level, a, b, end_type, [xarray, ...])
```
where
```
subdivision_level determines how many points to interpolate (1 doubles $#x in the above example). 
when a = b, this is the "s" paramater from the description (and the math paper below)
end_type is how you want to deal with the start and end points:
      3=join them up (loop). 2=tangent clamp, 1=end clamp, 0=simple join (refer "see also" below)
[xarray] any number of array references come next, ex [xarray,yarray,zarray]
```

# Example

```python
from jspline import jspline
js=jspline.make(1,0,0, 0 ,[[1, 2, 4, 5]])    # returns 1,2,3,4,5
# or
x=[ 50 ,250, 250, 50 ]
y=[ 50, 50, 250, 250 ]
js=jspline.make(1,0,0, 0 ,[x,y])    # Draws one of the the below
```
![Jsplines](http://www.chrisdrake.com/draw-some-jsplines.gif)

See Also http://faculty.cs.tamu.edu/schaefer/research/js.pdf for details.

# Installation
 
## Normal installation

```bash
pip install jspline
```

## Development installation

```bash
git clone https://github.com/gitcnd/jspline.git
cd jspline
pip install --editable .
```

## Author note

Be sure to check out [Airfoil Tools](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/add-in-announcement-hydrofoil-and-airfoil-tools-seeking-your/td-p/9453985), a Fusion 360 plugin, for which this module was written.
[![Airfoil Tools](http://www.chrisdrake.com/j-spline_airfoil.png)](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/add-in-announcement-hydrofoil-and-airfoil-tools-seeking-your/td-p/9453985)
