import cv2
import face_recognition

# Load Known Faces and Their Names Here
known_faces = {
    "sagar.jpeg": "aditya",
    "bhusan.jpeg": "Bhushan",
    "vishal.jpeg": "Vishal",
    "rohit.jpeg": "rohit"
}

known_face_encodings = []
known_face_names = []

for image_file, name in known_faces.items():
    image_path = "C:/Users/addis/Downloads/face rco/" + image_file
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)
    if face_encoding:
        known_face_encodings.append(face_encoding[0])
        known_face_names.append(name)
    else:
        print(f"No face detected in {image_file}. Skipping...")

# Camera
video_capture = cv2.VideoCapture(0)

try:
    while True:
        # Frames
        ret, frame = video_capture.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Face location in video frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Look at each face in frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check face from known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Box around face (yellow color)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 2)  # BGR: Yellow

            # Label the face
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)  # BGR: Yellow

        # Display the result
        cv2.imshow("video", frame)

        # Loop ends when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("Keyboard interrupt detected.")

finally:
    # Release camera
    video_capture.release()
    cv2.destroyAllWindows()
