import cv2
from config import Config
config = Config()


def feed(camera_index):

    vid = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    while True:
        _, frame = vid.read()

        height, width, _ = frame.shape
        # Height : 480
        # Width : 640

        thickness = 5
        start = (0, config.max_y)
        end = (width, config.max_y)
        color = (0, 0, 0)
        cv2.line(frame, start, end, color, thickness)

        text = 'Place vial caps on or above this line.'
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        word_thickness = 2
        coordinates = (25, 50)
        cv2.putText(frame, text, coordinates, font, font_scale, color, word_thickness, cv2.LINE_AA)


        cv2.imshow('Live feed', frame)

         # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    feed(0)