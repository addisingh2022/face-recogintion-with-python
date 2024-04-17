import cv2
import face_recognition

# Load Known Face Encodings and Names
known_face_encodings = []
known_face_names = []

# Load Known Faces and Their Names Here
known_personal_image = face_recognition.load_image_file("C:/Users/addis/Downloads/face rco/sagar.jpeg")
known_persona2_image = face_recognition.load_image_file("C:/Users/addis/Downloads/face rco/bhusan.jpeg")
known_persona3_image = face_recognition.load_image_file("C:/Users/addis/Downloads/face rco/vishal.jpeg")
known_persona4_image = face_recognition.load_image_file("C:/Users/addis/Downloads/face rco/rohit.jpeg")

known_personal_encoding = face_recognition.face_encodings(known_personal_image)[0]
known_persona2_encoding = face_recognition.face_encodings(known_persona2_image)[0]
known_persona3_encoding = face_recognition.face_encodings(known_persona3_image)[0]
known_persona4_encoding = face_recognition.face_encodings(known_persona4_image)[0]

known_face_encodings.extend([known_personal_encoding, known_persona2_encoding, known_persona3_encoding, known_persona4_encoding])

known_face_names.extend(["aditya", "Bhushan", "Vishal", "rohit"])

# Camera
video_capture = cv2.VideoCapture(0)

while True:
    # Frames
    ret, frame = video_capture.read()

    # Face location in video frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Look at each face in frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        # Check face from known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Box around face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the result
    cv2.imshow("video", frame)

    # Loop ends when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera
video_capture.release()
cv2.destroyAllWindows()
