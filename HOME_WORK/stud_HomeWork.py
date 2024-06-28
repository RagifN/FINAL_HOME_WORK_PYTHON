import argparse
import logging
from Student_Tasks.stud_001 import NameOfStudentsError, SubjectError, ScoreError
from Student_Tasks.stud_002 import Students

logging.basicConfig(filename='student.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:
        student = Students(args.name, args.csv_filename)
        student.add_score('Math', 6)

    except NameOfStudentsError:
        logging.error('Invalid student name format.')

    except SubjectError as e:
        logging.error(f'Invalid subject: {e.subject}')
        
    except ScoreError as e:
        logging.error(f'Invalid score: {e.score}')

if __name__ == '__main__':
    main()

# python my_script.py John subjects.csv - запуск из ком. строки
"""John - это имя студента"""