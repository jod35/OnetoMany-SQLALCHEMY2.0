from populate import db, program1, program2
from models import Program, Course

#retrieve objects
# print(program1.courses)
# print(program2.courses)


#delete objects

# db.delete(program2)
# db.commit()


program1 = db.query(Program).filter_by(name = "Bachelors in CS").first()


course3 = db.query(Course).filter_by(title='Data STRUCTURES AND ALGRITHMS').first()

db.delete(program1)

db.commit()