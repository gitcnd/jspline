# jspline

Multi-dimensional parameterized spline curves (snappiness parameter gives uniform cubic B-splines, four-point subdivision splines, uniform quintic B-splines, and everything in-between)

# Description
    
J-Splines are awesome: they're a class of spline curves that take a shape parameter, s. Setting s=1 yields uniform cubic B-spline curves, s=0 gives four-point subdivision curves, s=0.5 are uniform quintic B-splines - and more. "s" basically governs the "snappiness" of the curve.

`jspline`, lets you choose any combination of J-Spline parameters for any number of input arrays, with a range of different starting and ending schemes (eg: open or closed loops). Use it for 2D drawing, 3D graphics, or any other kind of interpolation you might need.

- See also my CPAN perl module that does the same: https://metacpan.org/pod/Math::JSpline

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
