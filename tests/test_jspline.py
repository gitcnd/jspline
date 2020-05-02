import jspline

# perl -MMath::JSpline -e 'my ($x)=&JSpline(1,0,0, 0 ,[1,2,4,5]);print join(" ",@{$x});' => 1 2 3 4 5
js=jspline.make(1,0,0, 0 ,[[1, 2, 4, 5]])
print(js)


x=[ 50 ,250, 250, 50 ]
y=[ 50, 50, 250, 250 ]

js=jspline.make(1,0,0, 0 ,[x,y])

print(js)
