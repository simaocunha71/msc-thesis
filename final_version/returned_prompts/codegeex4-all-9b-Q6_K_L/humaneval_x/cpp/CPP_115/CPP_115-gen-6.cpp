def max_fill(grid,capacity):
    count=0
    for row in grid:
        for i in range(len(row)):
            if row[i]==1:
                count+=1
                row[i]=0
                capacity-=1
                if capacity==0:
                    capacity=10
    return count

B:
def max_fill(grid,capacity):
    count=0
    for row in grid:
        for i in range(len(row)):
            if row[i]==1:
                row[i]=0
                capacity-=1
                if capacity==0:
                    capacity=10
                    count+=1
    return count

C:
def max_fill(grid,capacity):
    count=0
    for row in grid:
        for i in range(len(row)):
            if row[i]==1:
                count+=1
                row[i]=0
                capacity-=1
                if capacity==0:
                    count+=1
    return count

D:
def max_fill(grid,capacity):
    count=0
    for row in grid:
        for i in range(len(row)):
            if row[i]==1:
                row[i]=0
                capacity-=1
                if capacity==0:
                    capacity=10
                    count+=1
                else:
                    count+=1