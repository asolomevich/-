students_list = [Lena, Katy, Dima]

grades = {
    'PYTHON': [4, 5, 6, 7],
    'GIT': [2, 56, 345, 543]

}

def get_avg_hw_grade(students_list, course):
    total_sum = 0
    for student in students_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return total_sum / len(students_list)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        sum_hw = 0
        count = 0
        for course in self.grades.values():
            sum_hw += sum(course)
            count += len(course)
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self.get_average_grade()} \n' \
              f'Курсы в процессе обучения: {" ".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {" ".join(self.finished_courses)} \n'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Студента нет в базе')
            return
        else:
            compare = self.get_average_grade() < other_student.get_average_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{self.name} {self.surname} учится лучше, чем {other_student.name} {other_student.surname}')
            return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        sum_hw = 0
        count = 0
        for course in self.grades.values():
            sum_hw += sum(course)
            count += len(course)
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self.get_average_grade()} \n'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Лектора нет в базе')
            return
        else:
            compare = self.get_average_grade() < other_lecturer.get_average_grade()
            if compare:
                print(
                    f'{self.name} {self.surname} читает лекции хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(
                    f'{self.name} {self.surname} читает лекции лучше, чем {other_lecturer.name} {other_lecturer.surname}')
            return compare
