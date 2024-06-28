class NameOfStudentsError(Exception):
    def __init__(self, message="Студента с таким именем нет. Оно должно начинаться с заглвной буквы и состоять исключительно из букв."):
        self.message = message
        super().__init__(self.message)

class SubjectError(Exception):
    def __init__(self, subject_name):
        self.message = f"Предмет '{subject_name}' Не найден в файле CSV."
        super().__init__(self.message)

class ScoreError(Exception):
    def __init__(self, score, score_type="Оценка"):
        self.message = f"{score_type} '{score}' Недействителен!!! Оценки должны быть только от 2 до 5, а результаты тестов только от 0 до 100."
        super().__init__(self.message)