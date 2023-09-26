# Converting any given number into different sizes in B, KB, MB, GB, and TB.


the_number = int(input("Please enter the number of Bytes:"))
sizes = ["Bytes", "KiloBytes", "Megabytes", "Gigabytes", "Terabytes"]
counter = 0

while the_number >= 1e3 and counter < len(sizes)-1:
    the_number /= 1e3
    counter += 1

print(the_number, sizes[counter])
