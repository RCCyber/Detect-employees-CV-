import cv2

cap = cv2.VideoCapture('Camera.mp4')
count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        rectangle_frame = cv2.rectangle(frame, (115, 210), (350, 445), (200, 0, 0), 2)
        rectangle_frame = rectangle_frame[210:445, 115:350]
        new_frame_size = cv2.resize(rectangle_frame, (116, 116))
        cv2.imwrite('./images/frame{:d}.jpg'.format(count), new_frame_size)
        count += 15  # i.e. at 15 fps, this advances one second
        cap.set(cv2.CAP_PROP_POS_FRAMES, count)
    else:
        cap.release()
        break
