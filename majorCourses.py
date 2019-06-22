import urllib.request
import re

collegeMajors = {}

majorsFile = open('majorData.csv', 'r')
majorsFile.readline()

for line in majorsFile:
    cells = line.split(',')
    majorName = cells[0]
    majorCode = cells[1]
    majorNum = cells[2]
    collegeMajors[majorName] = majorCode + majorNum

majorsFile.close()

print(collegeMajors)

#soughtMajor = input("Major: ")

#courses = []

majorsAndCourses = {}

standardCode4 = r"[A-Z]{4} \d{4}"
standardCode3 = r"[A-Z]{3} \d{4}"
standardCode2 = r"[A-Z]{2} \d{4}"

withOtherSymbols4 = r"[A-Z]{4} \d{4}([^A-Z]* \d{4})+"
withOtherSymbols3 = r"[A-Z]{3} \d{4}([^A-Z]* \d{4})+"
withOtherSymbols2 = r"[A-Z]{2} \d{4}([^A-Z]* \d{4})+"

otherCourseCode = withOtherSymbols4 + "|" + withOtherSymbols3 + "|" + withOtherSymbols2
standardCourseCode = standardCode4 + "|" + standardCode3 + "|" + standardCode2

# testText = "CS 1110 <hr> Y 23 </hr=2911> BIOL 1210, and/or 2220, 2240 or 2502 STS 3249, 2398"
# finder = re.compile(otherCourseCode)
#
# for match in finder.finditer(testText):
#         print(match.group())

#try:
for major in collegeMajors.keys():
    courses = []
    code = collegeMajors[major]
    print(code)
    url = "http://records.ureg.virginia.edu/preview_program.php?catoid=45&" + code
    majorPage = urllib.request.urlopen(url)
    majorText = majorPage.read().decode('utf-8')
    standardCourseFinder = re.compile(standardCourseCode)
    for match in standardCourseFinder.finditer(majorText):
        stringMatch = match.group(0)
        if (stringMatch[0:7] != "VA 2290") and (stringMatch not in courses) and (stringMatch[0] != "<"):
            courses.append(match.group(0))
    otherCourseFinder = re.compile(otherCourseCode)
    for match in otherCourseFinder.finditer(majorText):
        stringMatch = match.group(0)
        if (stringMatch[0:7] != "VA 2290") and (stringMatch not in courses) and (stringMatch[0] != "<"):
            courses.append(match.group(0))
    courses.sort()
    majorsAndCourses[major] = courses
dataFile = open('data.txt', 'w')
for item in majorsAndCourses.keys():
        print(item + ": " + str(majorsAndCourses[item]) + "\n", file=dataFile)


# except:
#     print("No such major. Remember to type major name exactly as appears.")
