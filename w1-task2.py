import cv2 as cv

capture = cv.VideoCapture("Images/Gandalf.mp4")

while True:

  retval, frame = capture.read() # retval is bool for successful read_

  # Exit loop once end of the video is reached_

  if not retval:

    break

  cv.imshow("Gandalf Laugh", frame)

  if cv.waitKey(17) ==ord('d'): # Close if 'd' is pressed_

    break

capture.release()

cv.destroyAllWindows()