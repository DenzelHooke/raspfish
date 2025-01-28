from flask import Flask, Response
import cv2 as opencv

videoInt = 1 

app = Flask(__name__)
camera = opencv.VideoCapture(videoInt | 0)

def generate_frames():
    while True:
        success, frame = camera.read()  # Read a frame from the camera
        if not success:
            break
        else:
            # Encode the frame as JPEG
            ret, buffer = opencv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def home():
    return "Hello world from Flask"


@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")




    
    camera.release()
    opencv.destroyAllWindows()


    return "Video endpoint :)"




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
    
 


