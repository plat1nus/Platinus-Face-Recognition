import face_recognition


class FaceDetector:
    def __init__(self, version):
        self.version = version
        self.paths = []
        self.names = []
        self.image = None
        self.image_encoding = None
        self.mode = None

    def get_original_face(self):
        print(f"Platinus face recognition. version={self.version}")
        self.paths.append(input("Введите путь до изображения с нужным лицом: "))
        self.names.append(input("Введите имя: "))
        try:
            self.image = face_recognition.load_image_file(self.paths[0])  # temporarily
            self.image_encoding = face_recognition.face_encodings(self.image)[0]
            return self.image_encoding, self.names
        except FileNotFoundError:
            raise FileNotFoundError("Incorrect path to image")