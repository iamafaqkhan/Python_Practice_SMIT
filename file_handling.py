class StudentRecord:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def save_to_files(self):
        with open('Student.txt', 'a') as f:
            f.write(f'{self.name} : {self.id} : {self.marks}')

    def search_student(self, student_id):

        with open('Student.txt', 'r') as f:

            for lines in f:

                if not lines.strip():
                    continue

                data = lines.split(':')

                name = data[0].strip()
                id = data[1].strip()
                marks = data[2].strip()

                if id == str(student_id):
                    print(f'Student Found! \n {name} : {id} : {marks}')
                else:
                    'Student Not Found!'

    @staticmethod
    def display():
        with open('Student.txt', 'r') as f:
            print(f.read())

        
s1 = StudentRecord('Afaq', 359, 99)
s2 = StudentRecord('Ali', 360, 95)

s1.save_to_files()
s2.save_to_files()

s1.search_student(340)

# s2.display()



    