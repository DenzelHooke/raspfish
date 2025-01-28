import cv2



camera = cv2.VideoCapture(0)


while True:
    # Reading video frame
    valid, frame = camera.read()

    if not valid:
        print("Failed to grab frame")
        break

    print('Displaying video frame ')
    cv2.imshow("Video Frame", frame)

    # Break when 'q' is pressed
    # Ord represents the ordinal value of each letter. 
    # Each letter has a numerical value associated with it
    # -that we can use to track. 


    if cv2.waitKey(1) == ord('q'):
        break


# release camera
camera.release()  

# Close all windows 
cv2.destroyAllWindows() 





   

