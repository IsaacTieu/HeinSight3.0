import cv2


def feed(camera_index):

    vid = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    while True:
        _, frame = vid.read()

        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imshow('Live feed', frame)

         # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    feed(0)