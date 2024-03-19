import cv2
import datetime

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

while True:
    (Flow, gray) = camera.read()

    if not Flow:
        break

    gun = gun_cascade.detectMultiScale(gray, 1.15, 5)
    try:

        (x, y, w, h) = gun[-1]
        gray = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = gray[y:y + h, x:x + w]

        if len(gun) > 0:
            cv2.putText(gray, "Weapon", (x + 15, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (20, 20, 255), 2)
            print("gun detected")
        else:
            print("gun not detected")
    except:
        None
    cv2.putText(gray, datetime.datetime.now().strftime("%A %d %B %Y %I: %M:%S%p"), (10, gray.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.imshow("Cam1", gray)

    if cv2.waitKey(10) & 0xFF == (ord('q')):
        break

camera.release()
cv2.destroyAllWindows()