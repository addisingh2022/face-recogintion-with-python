import cv2
import face_recognition

#Load Know Face Encoding and Names

Know_face_encodings =[]
Know_face_names = []

#Load Knows Faces and There Name  Here

Know_personal_image = face_recognition.load_image_file("C:/Users/addis/Downloads/face rco/sagar.jpeg")
Know_persona2_image = face_recognition.load_image_file("C:/Users/addis/Downloads/face rco/bhusan.jpeg")
Know_persona3_image = face_recognition.load_image_file("C:/Users/addis/Downloads/face rco/vishal.jpeg")
Know_persona4_image = face_recognition.load_image_file("C:/Users/addis/Downloads/face rco/rohit.jpeg")

Know_Personal_encoding = face_recognition.face_encodings(Know_personal_image)[0]
#Know_Persona2_encoding = face_recognition.face_encodings(Know_persona2_image)[0]
#Know_Persona3_encoding = face_recognition.face_encodings(Know_persona3_image)[0]
#Know_Persona4_encoding = face_recognition.face_encodings(Know_persona4_image)[0]

Know_face_encodings.append(Know_Personal_encoding)
#Know_face_encodings.append(Know_Persona2_encoding)
#Know_face_encodings.append(Know_Persona3_encoding)
#Know_face_encodings.append(Know_Persona4_encoding)

Know_face_names.append("aditya")
#Know_face_names.append("Bhushan")
#know_face_names.append("Vishal")
#Know_face_names.append("rohit")


#Camera
Vedio_capture = cv2.VideoCapture(0)

while True:
    #frames
    ret, frame = Vedio_capture.read()

    #face loaction in  vedio frame 

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame,face_locations)

    #look  each face in frame 

    for(top,right,bottom,left), face_encoding in zip(face_locations,  face_encodings):
        
        #check face from know faces
        matches = face_recognition.compare_faces(Know_face_encodings, face_encoding)
        name = "unkown"

        if True in matches:
            first_match_index = matches.index(True)
            name = Know_face_names[first_match_index]

            #box around face 
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left, top - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            #display the result
            cv2.imshow("video", frame)

            # loop end when q is pressed
            if cv2.waitKey(1) &  0xFF == ord("q"):
                break

            # realse camera
            Vedio_capture.release()
            cv2.destroyAllWindows()

