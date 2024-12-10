class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lect(self, lecturer, course, grade):
        if not (1 <= grade <= 10):
            return 'оценка должна быть от 1 до 10'
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        if total_courses > 0:
            avarage = total_grades / total_courses
            return round(avarage, 1)
        else:
            return 0
    
    def __lt__(self, student):
        return self.average_grade() < student.average_grade()

    def __str__(self):
        return f'Студент \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.average_grade()} \nКурсы в процессе обучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'        


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        if total_courses > 0:
            avarage = total_grades / total_courses
            return round(avarage, 1)
        else:
            return 0

    def __lt__(self, lecturer):
        return self.average_grade() < lecturer.average_grade()

    def __str__(self):
        return f'Лектор \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Эксперт \nИмя: {self.name} \nФамилия: {self.surname}'


def average_lectures(lecturers, course):
    count = 0
    total_grades = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total_grades += lecturer.average_grade()
            count += 1
    return total_grades / count

def average_students(students, course):
    count = 0
    total_grades = 0
    for student in students:
        if course in student.courses_in_progress:
            total_grades += student.average_grade()
            count += 1
    return total_grades / count


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Ivan', 'Gerold', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Alex', 'Ivanov')
cool_lecturer2.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)

cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer.rate_hw(best_student2, 'Python', 5)
cool_reviewer.rate_hw(best_student2, 'Python', 9)

best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 9)
best_student.rate_lect(cool_lecturer, 'Python', 7)

best_student.rate_lect(cool_lecturer2, 'Python', 10)
best_student.rate_lect(cool_lecturer2, 'Python', 6)
best_student.rate_lect(cool_lecturer2, 'Python', 7)

lecturers = [cool_lecturer, cool_lecturer2]
students = [best_student, best_student2]

avg_homework = average_students(students, 'Python')
avg_lectures = average_lectures(lecturers, 'Python')

print(cool_reviewer)
print(cool_lecturer)
print(cool_lecturer2)
print(best_student)
print(best_student2)

if (cool_lecturer < cool_lecturer2):
    print('Средняя оценка лектора', cool_lecturer.name, cool_lecturer.surname, 'меньше чем у', cool_lecturer2.name, cool_lecturer2.surname)
else:
    print('Средняя оценка лектора', cool_lecturer2.name, cool_lecturer2.surname, 'меньше чем у', cool_lecturer.name, cool_lecturer.surname)

if (best_student < best_student2):
    print('Средняя оценка студента', best_student.name, best_student.surname, 'меньше чем у', best_student2.name, best_student2.surname)
else:
    print('Средняя оценка студента', best_student2.name, best_student2.surname, 'меньше чем у', best_student.name, best_student.surname)

print(f"Средняя оценка за домашние задания: {avg_homework}")
print(f"Средняя оценка за лекции: {avg_lectures}")