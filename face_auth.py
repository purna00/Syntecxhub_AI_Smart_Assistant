
import cv2
import numpy as np
from pathlib import Path
import time


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "face_model.yml"
NAME_PATH = MODEL_DIR / "user_name.txt"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

FACE_CASCADE = cv2.CascadeClassifier(
    str(Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml")
)


def get_camera():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not camera.isOpened():
        camera.release()
        camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open the webcam.")
        return None

    return camera


def detect_faces(gray_frame):
    return FACE_CASCADE.detectMultiScale(
        gray_frame,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )


def register_face():
    if FACE_CASCADE.empty():
        print("Error: OpenCV face detector could not be loaded.")
        return

    name = input("Enter your full name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    camera = get_camera()

    if camera is None:
        return

    face_samples = []
    required_samples = 60
    last_capture = 0

    print("\nFace registration started.")
    print("Look at the camera and move your face slightly.")
    print("Press Q to cancel registration.")

    try:
        while len(face_samples) < required_samples:
            success, frame = camera.read()

            if not success:
                print("Could not read from webcam.")
                break

            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detect_faces(gray)

            for (x, y, w, h) in faces:
                cv2.rectangle(
                    frame, (x, y), (x + w, y + h), (0, 255, 0), 2
                )

                current_time = time.time()

                if current_time - last_capture >= 0.12:
                    face = gray[y:y + h, x:x + w]
                    face = cv2.resize(face, (200, 200))
                    face_samples.append(face)
                    last_capture = current_time

                break

            cv2.putText(
                frame,
                f"Samples: {len(face_samples)}/{required_samples}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.imshow("Jarvis - Face Registration", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()

    if len(face_samples) < 15:
        print("Not enough face samples. Please register again.")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    labels = np.zeros(len(face_samples), dtype=np.int32)
    recognizer.train(face_samples, labels)
    recognizer.write(str(MODEL_PATH))
    NAME_PATH.write_text(name, encoding="utf-8")

    print("\nRegistration completed successfully!")
    print(f"Registered user: {name}")
    print(f"Face model saved to: {MODEL_PATH}")


def authenticate_face():
    if not MODEL_PATH.exists() or not NAME_PATH.exists():
        print("No registered face found.")
        print("Choose option 1 to register your face first.")
        return False

    if FACE_CASCADE.empty():
        print("Error: OpenCV face detector could not be loaded.")
        return False

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(str(MODEL_PATH))

    user_name = NAME_PATH.read_text(encoding="utf-8").strip()

    camera = get_camera()

    if camera is None:
        return False

    consecutive_matches = 0
    required_matches = 8
    start_time = time.time()
    timeout_seconds = 30
    authenticated = False

    print(f"\nJarvis is checking your face, {user_name}...")
    print("Look at the camera. Press Q to cancel.")

    try:
        while time.time() - start_time < timeout_seconds:
            success, frame = camera.read()

            if not success:
                print("Could not read from webcam.")
                break

            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detect_faces(gray)

            status = "No face detected"
            color = (0, 0, 255)

            if len(faces) > 0:
                x, y, w, h = max(
                    faces, key=lambda box: box[2] * box[3]
                )

                face = gray[y:y + h, x:x + w]
                face = cv2.resize(face, (200, 200))

                label, confidence = recognizer.predict(face)

                if label == 0 and confidence < 60:
                    consecutive_matches += 1
                    status = f"Recognizing: {consecutive_matches}/{required_matches}"
                    color = (0, 255, 0)
                else:
                    consecutive_matches = 0
                    status = "Face not recognized"
                    color = (0, 0, 255)

                cv2.rectangle(
                    frame, (x, y), (x + w, y + h), color, 2
                )

            cv2.putText(
                frame,
                status,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                color,
                2
            )

            cv2.imshow("Jarvis - Face Authentication", frame)

            if consecutive_matches >= required_matches:
                authenticated = True
                break

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()

    if authenticated:
        print(f"\nAccess granted! Welcome, {user_name}.")
        return True

    print("\nAccess denied or authentication timed out.")
    return False
