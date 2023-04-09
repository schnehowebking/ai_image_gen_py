seriesfisrtNumber = float(input("Enter 1st number of the arithmatic series "))

distance = float(input("Enter Distance of arithmatic serise "))

nthTermOfSeries = float(input("Enter the N'th Number "))


a = nthTermOfSeries-1
b =a*distance
c = b+seriesfisrtNumber


nthNumberOfSeries = str(c+b)

sumofTheSerise = str((nthTermOfSeries*((2*seriesfisrtNumber)+((nthTermOfSeries-1)*distance)))/2)


print("n'th Number of the serise is " + nthNumberOfSeries)
print("Sum of the serise is " +sumofTheSerise)

