import cv2, time, pandas
from datetime import datetime

# Variables
first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

# Define capture device
video=cv2.VideoCapture(0)

while True:
   
    # Capture a frame
    check, frame = video.read()
    
    # Start status as no movement
    status=0
    
    # Make the frame gray and apply blur
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    # Set up the reference first frame
    if first_frame is None:
        first_frame=gray
        continue

    # Calculate delta between first frame and gray frame
    delta_frame=cv2.absdiff(first_frame,gray)
    
    # Define threshholds
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    # Find contours.
    # Classify as movement if it applies.
    # Draw green box when is movement.
    contours, hierarchy =cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1

        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    # Add status to the list and maintain only last two status
    status_list.append(status)
    status_list=status_list[-2:]

    # Check wheter it changes from movement to no movement and vice versa
    # Status 0 -> 1 = Start movement, 1 -> 0 Finish movement
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    # Show realtime captures
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    # Key to end capture session
    key=cv2.waitKey(1)

    # Finish capture session
    # When status = 1, means we have an open start time waiting for a finish time, so is necessary to close this time span
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

# Build a data frame for movement times
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

# Export df to a csv
df.to_csv("Times.csv")

# release videos and windows
video.release()
cv2.destroyAllWindows
