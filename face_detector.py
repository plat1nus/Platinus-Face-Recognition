import face_recognition


class FaceDetector:
    def __init__(self, version):
        self.version = version
        self.paths = []
        self.names = []
        self.images = []
        self.image_encodings = []
        self.mode = None

    def get_original_face(self):
        print(f"Platinus face recognition. version={self.version}")
        n = int(input("Введите количество(ЧИСЛО) изображений с неповторяющимися лицами: "))
        print("Вводите путь к изображению и имя человека на фото.")
        for i in range(n):
            self.paths.append(input("Введите путь до изображения с нужным лицом: "))
            self.names.append(input("Введите имя: "))
        try:
            self.images = [face_recognition.load_image_file(path) for path in paths]  # temporarily
            self.image_encodings = face_recognition.face_encodings(self.image)[0]
            return self.image_encoding, self.names
        except FileNotFoundError:
            raise FileNotFoundError("Вы ввели несуществущий путь к изображению")