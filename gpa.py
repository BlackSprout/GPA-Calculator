from math import ceil


#display expected gpa
def sgpa(l):
    #l=[isa1[phy,cs,math,eee,mech,evs],isa2[phy,cs,math,eee,mech,evs],ass[],esa[],credit[]]
    
    total = list(map(lambda x,y,z,a:(x+y+z+a)/2,l[0],l[1],l[2],l[3]))
    grade = list(map(lambda x:ceil(x//10)+1,total))
    
    
    print("GRADES: ",grade)
    gpas = sum(list(map(lambda x,y:x*y,l[4],grade)))/sum(l[4])
    return gpas


#highest possible gpa based on internals
def how_much(l):
    # l =[[isa1],[isa2],[ass]] #phy,cs,math,eee,mech,evs
    p = list(map(lambda x,y,z:50 - (x+y+z)/2,l[0],l[1],l[2]))
    k1 = list(map(lambda x : (100 - x)//10 +1 , p))
    k2 = list(map(lambda x :100 - ((100 - x)%10)*2 , p))
    print("HIGHEST SGPA POSSIBLE = ",k1)
    print("TO GET THAT U NEED = ",k2)
    return f"HIGHEST SGPA POSSIBLE = {k1} and TO GET THAT U NEED = {k2}"




#cgpa calculation 
def cgpa2(l):
    # l =[[sgpa,credit]]
    

    print("CGPA = ",sum(map(lambda x : int(x[0])*(x[1]) ,l))/sum(map(lambda x : x[1] ,l)))


def cgpa(grades_credits):
    # Convert grades to points
    grade_points = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 0}
    total_points = 0
    total_credits = 0

    for grade, credit in grades_credits:
        total_points += grade_points[grade] * credit
        total_credits += credit

    return total_points / total_credits if total_credits != 0 else 0