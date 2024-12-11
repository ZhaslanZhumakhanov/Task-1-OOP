from jwt.utils import number_to_bytes


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за домашние задания:{self.average_rating(): .1f} \n"
                f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}  \n"
                f"Завершенные курсы: {", ".join(self.finished_courses)} \n")

    def __eq__(self, other):
        return self.average_rating() == other.average_rating()

    def __ne__(self, other):
        return self.average_rating() != other.average_rating()

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __gt__(self, other):
        return self.average_rating() > other.average_rating()

    def __le__(self, other):
        return self.average_rating() <= other.average_rating()

    def __ge__(self, other):
        return self.average_rating() >= other.average_rating()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in lecturer.courses_attached) and (course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
         rating = 0
         number_of_grades = 0

         for course, grades in self.grades.items():
            rating += sum(grades)
            number_of_grades += len(grades)

         if number_of_grades > 0:
            return rating / number_of_grades
         else:
            return 0

    def average_course_rating(self, course):
        grades = self.grades[course]

        if len(grades) > 0:
            return sum(grades) / len(grades)
        else:
            return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за лекции:{self.average_rating(): .1f} \n")

    def __eq__(self, other):
        return self.average_rating() == other.average_rating()

    def __ne__(self, other):
        return self.average_rating() != other.average_rating()

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __gt__(self, other):
        return self.average_rating() > other.average_rating()

    def __le__(self, other):
        return self.average_rating() <= other.average_rating()

    def __ge__(self, other):
        return self.average_rating() >= other.average_rating()

    def average_rating(self):
        rating = 0
        number_of_ratings = 0

        for course, grades in self.grades.items():
            rating += sum(grades)
            number_of_ratings += len(grades)

        if number_of_ratings > 0:
            return rating / number_of_ratings
        else:
            return 0

    def average_course_rating(self, course):
        grades = self.grades[course]

        if len(grades) > 0:
            return sum(grades) / len(grades)
        else:
            return 0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname}")

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and (course in self.courses_attached) and (course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_course_grade_students(students: [Student], course):
    grade = 0
    for student in students:
        grade += student.average_course_rating(course)
    return grade / len(students)

def average_course_grade_lecturers(lecturers: [Lecturer], course):
    grade = 0
    for lecturer in lecturers:
        grade += lecturer.average_course_rating(course)
    return grade / len(lecturers)

# Заводим 2-ух студентов
best_student = Student('Ruoy', 'Eman', 'man')
best_student.finished_courses += ['Python']
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Pascal']
best_student.courses_in_progress += ['Java']

student_2 = Student('Vin', 'Diezel', 'man')
student_2.finished_courses += ['Python']
student_2.finished_courses += ['Git']
student_2.courses_in_progress += ['Pascal']
student_2.courses_in_progress += ['Java']

# Заводим 2-ух лекторов
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

cool_lecturer_2 = Lecturer('Tom', 'Hanks')
cool_lecturer_2.courses_attached += ['Python']
cool_lecturer_2.courses_attached += ['Git']

# Заводим 2-ух ревьюверов
cool_reviewer = Reviewer('Leo', 'Dicaprio')
cool_reviewer.courses_attached += ['Java']
cool_reviewer.courses_attached += ['Pascal']

cool_reviewer_2 = Reviewer('Leo', 'Dicaprio')
cool_reviewer_2.courses_attached += ['Java']
cool_reviewer_2.courses_attached += ['Pascal']

# Ревьюверы выставляют оценки студентам
cool_reviewer.rate_hw(best_student, 'Pascal', 10)
cool_reviewer.rate_hw(best_student, 'Pascal', 20)
cool_reviewer.rate_hw(best_student, 'Java', 7)

cool_reviewer_2.rate_hw(student_2, 'Pascal', 30)
cool_reviewer_2.rate_hw(student_2, 'Pascal', 40)
cool_reviewer_2.rate_hw(student_2, 'Java', 7)

# Студенты выставляют оценки лекторам
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 15)
best_student.rate_hw(cool_lecturer, 'Python', 20)

best_student.rate_hw(cool_lecturer, 'Git', 10)
best_student.rate_hw(cool_lecturer, 'Git', 15)

student_2.rate_hw(cool_lecturer_2, 'Python', 1)
student_2.rate_hw(cool_lecturer_2, 'Python', 2)
student_2.rate_hw(cool_lecturer_2, 'Python', 3)

student_2.rate_hw(cool_lecturer_2, 'Git', 10)
student_2.rate_hw(cool_lecturer_2, 'Git', 15)

print(f"Первый студент \n{best_student}")
print(f"Второй студент \n{student_2}")

print(f"Первый лектор \n{cool_lecturer}")
print(f"Второй лектор \n{cool_lecturer_2}")

print(best_student < student_2)
print(cool_lecturer == cool_lecturer_2)

print(best_student.grades)
print(cool_lecturer.grades)

print(best_student.average_course_rating('Pascal'))

print(average_course_grade_students([best_student, student_2], 'Pascal'))

print(average_course_grade_lecturers([cool_lecturer, cool_lecturer_2], 'Python'))