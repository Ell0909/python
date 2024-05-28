
import csv

file = open("notephone.csv","a")

Name = input("Name: ")
Number = input("Number: ")

writer = csv.writer(file)
writer.writerow([Name,Number])


file.close
