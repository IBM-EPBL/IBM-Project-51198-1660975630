import cv2
from playsound import playsound
from twilio.rest import Client


fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("Fire is detected 🔥🔥")
        playsound('audio.mp3')


        account_sid = 'ACf232c8d290c2e56b760b27dcfe4a481e'
        auth_token = '329e940af6e7ee375f8fd4a2a94968bc'
        twilio_number = '+19803757860'
        target_keys = '+919962828967'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="yelaii pathikichuleyyy 🔥",
            from_=twilio_number,
            to=target_keys
        )
        print(message.body)
        exit()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
