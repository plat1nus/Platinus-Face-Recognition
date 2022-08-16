import face_recognition
import cv2
import numpy as np
from info import VERSION
from face_detector import FaceDetector


def main():
    detector = FaceDetector(VERSION)

    image_encoding, names = detector.get_original_face()

    process_this_frame = True
    face_locations = []
    face_names = []
    name = ""
    cap = cv2.VideoCapture(0)

    while True:
        scs, img = cap.read()

        if process_this_frame:
            img_resized = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

            img_resized_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(img_resized_rgb)
            face_encodings = face_recognition.face_encodings(img_resized_rgb, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces([image_encoding], face_encoding)
                face_distances = face_recognition.face_distance([image_encoding], face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = names[best_match_index]
                face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.rectangle(img, (left, top), (right, top - 30), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (left + 6, top - 6), font, 1.0, (255, 255, 255), 1)

        process_this_frame = not process_this_frame

        cv2.imshow("platinus-recognition", img)

        if cv2.waitKey(1) and 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
