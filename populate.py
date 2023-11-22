from connect import engine, db
from models import Program, Course



program1 = Program(
    name = "Bachelors in CS",
    years_of_study =3
)

program2 = Program(
    name = "Bachelors in Business",
    years_of_study =3
)

# saving programs
# db.add_all(
#     [program1,program2]
# )

# db.commit()

# query for the created programs
program1 = db.query(Program).filter_by(name = "Bachelors in CS").first()

program2 = db.query(Program).filter_by(name = "Bachelors in Business").first()


#create course objects
course1 = Course(
    title ="Database Management Systems",
    code = "CS 102"
)


course2 = Course(
    title ="Data SCIENCE",
    code = "CS 103"
)


course3 = Course(
    title ="Data STRUCTURES AND ALGRITHMS",
    code = "CS 110"
)

course4 = Course(
    title ="Businnes communication",
    code = "BS 123"
)


# adding child object to parent
# program1.courses.append(course1)
# program1.courses.append(course2)
# program1.courses.append(course3)
# program2.courses.append(course4)


db.commit()