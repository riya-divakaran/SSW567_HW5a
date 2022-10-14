def classifyTriangle(a,b,c):

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers 
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'   
    # now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    elif (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
      return 'Isoceles'

