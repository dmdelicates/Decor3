from tools import logger

path = 'log1.txt'


class Student:
    @logger(path)
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    @logger(path)
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    @logger(path)
    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    @logger(path)
    def avg_grades(self):
        sum_grades = 0
        len_grades = 0
        for grade in self.grades.values():
            for g in grade:
                sum_grades += g
            len_grades += len(grade)
        if len_grades == 0:
            res = 0
        else:
            res = round(sum_grades / len_grades, 1)
        return res

    @logger(path)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades()}'
        return res

    @logger(path)
    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            res = 'Студента можно сравнивать только со студентом'
        else:
            res = self.avg_grades() < other_student.avg_grades()
        return res


class Mentor:
    @logger(path)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    @logger(path)
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    @logger(path)
    def avg_grades(self):
        sum_grades = 0
        len_grades = 0
        for grade in self.grades.values():
            for g in grade:
                sum_grades += g
            len_grades += len(grade)
        if len_grades == 0:
            res = 0
        else:
            res = round(sum_grades / len_grades, 1)
        return res

    @logger(path)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.avg_grades()}'
        return res

    @logger(path)
    def __lt__(self, other_lector):
        if not isinstance(other_lector, Lecturer):
            res = 'Лектора можно сравнивать только с лектором'
        else:
            res = self.avg_grades() < other_lector.avg_grades()
        return res


class Reviewer(Mentor):

    @logger(path)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    @logger(path)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


@logger(path)
def avg_grades_all_students(list_students, course):
    sum_all = 0
    len_all = 0
    for student in list_students:
        if isinstance(student, Student):
            sum_all += student.avg_grades()
            len_all += 1
    if len_all == 0:
        res = 0
    else:
        res = round(sum_all / len_all)
    return res


@logger(path)
def avg_grades_all_lectors(list_lectors, course):
    sum_all = 0
    len_all = 0
    for lector in list_lectors:
        if isinstance(lector, Lecturer):
            sum_all += lector.avg_grades()
            len_all += 1
    if len_all == 0:
        res = 0
    else:
        res = round(sum_all / len_all)
    return res


student1 = Student('Ruoy', 'Eman', 'm')
student1.courses_in_progress += ['Python']

student2 = Student('Ivan', 'Ivanov', 'm')
student2.courses_in_progress += ['Python']

expert1 = Reviewer('Petr', 'Smit')
expert1.courses_attached.append('Python')
expert2 = Reviewer('Nataly', 'Egorova')
expert2.courses_attached.append('Python')

expert1.rate_hw(student1, 'Python', 4)
expert1.rate_hw(student1, 'Python', 6)
expert1.rate_hw(student2, 'Python', 10)

expert2.rate_hw(student1, 'Python', 9)

lector1 = Lecturer('Dmitry', 'Calt')
lector1.courses_attached.append('Python')

lector2 = Lecturer('Kira', 'Palm')
lector2.courses_attached.append('Python')

student1.rate_lector(lector1, 'Python', 5)
student2.rate_lector(lector1, 'Python', 4)
student1.rate_lector(lector2, 'Python', 9)

print(student1.__dict__)
print(student2.__dict__)

print(lector1.__dict__)
print(lector2.__dict__)

print(avg_grades_all_students([student1, student2], 'Python'))

print(avg_grades_all_lectors([lector1, lector2], 'Python'))

