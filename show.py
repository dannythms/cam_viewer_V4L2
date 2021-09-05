import cv2

cam_index = input('Enter Camera Index: ')
cap = cv2.VideoCapture(int(cam_index))

print('0 = direct\n1 = B/W with Normalization\n2 = B/W')
img_set = input('Enter Cam Preference: ')

if img_set == '':
    img_set = 0

frame_des = 'Direct'

while True:

    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    if int(img_set) == 1:
        frame_des = 'B/W with Normalization'
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.normalize(frame, frame, 0, 255, cv2.NORM_MINMAX)
    elif int(img_set) == 2:
        frame_des = 'B/W'
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow(frame_des, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
