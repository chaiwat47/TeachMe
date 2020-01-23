# find minimum point1 for  y=x^2
print("GD function for y=x^2")
def find_min_point1(learning_rate,epsilon,x_before,dif):
    while(dif>epsilon):
        x_updated=x_before-learning_rate*(2*x_before)
        dif=abs(x_before-x_updated)
        x_before=x_updated
    return x_updated
#testf1
print("test for minimum point of y=x^2")
test1=find_min_point1(learning_rate=0.1, epsilon=0.0000001, x_before=5, dif=1)
print("test_1=",test1)

test2=find_min_point1(learning_rate=0.01, epsilon=0.0000001, x_before=5, dif=1)
print("test_2=",test2)

test3=find_min_point1(learning_rate=0.5, epsilon=0.0000001, x_before=5, dif=1)
print("test_3=",test3)

# find minimum point2 for  y=(x+1)^2
print("GD function for y=(x+1)^2")
def find_min_point2(learning_rate,epsilon,x_before,dif):
    while(dif>epsilon):
        x_updated=x_before-learning_rate*(2*(x_before+1))
        dif=abs(x_before-x_updated)
        x_before=x_updated
    return x_updated

#testf2
print("test for minimum point of y=(x+1)^2")
test1=find_min_point2(learning_rate=0.1, epsilon=0.0000001, x_before=5, dif=1)
print("test_x1=",test1)

test2=find_min_point2(learning_rate=0.01, epsilon=0.0000001, x_before=5, dif=1)
print("test_x2=",test2)

test3=find_min_point2(learning_rate=0.5, epsilon=0.0000001, x_before=5, dif=1)
print("test_x3=",test3)