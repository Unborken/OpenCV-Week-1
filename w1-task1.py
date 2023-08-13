import cv2 as cv

def main():

  logo = cv.imread("Images/USRC.png")

  cv.imshow("USRC", logo)

  cv.waitKey(0)

if __name__ == "__main__":

  main()