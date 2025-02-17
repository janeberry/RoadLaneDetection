import cv2
import numpy as np

# Load the video
src = cv2.VideoCapture('/Users/jane/Desktop/dev/OpenCV/data/drive_cam.mp4')

show_lanes = True

def region_of_interest(img):
    height, width, _ = img.shape
    
    # Define the vertices of the polygon (Half of region)
    polygon = np.array([
        [(0, height), (width//2, height//2), (width, height)]
    ])

    # Create an empty mask to overlay the region of interest
    mask = np.zeros_like(img)
    
    # Fill the polygon area with Yellow
    cv2.fillPoly(mask, polygon, (0,255,255))

    # Non-Poly -> not mask
    inverted_mask = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(img, inverted_mask)
    result = cv2.add(result, mask)
    
    return result

def drawLane(img, edges):
    # Detect Lanes by Hough Transform
    lanes = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=100, maxLineGap=50)
    
    # Draw the detected lines on the original image
    if lanes is not None:
        for line in lanes:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)  # Draw in green color

    return img

while True:
    ret, frame = src.read()
    
    if not ret:
        break
    
    # Apply region of interest to filter the area
    filtered_edges = region_of_interest(frame)

    # Convert the filtered image to grayscale
    gray_frame = cv2.cvtColor(filtered_edges, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray_frame, 50, 150)

    # Detect and draw lanes on the original image
    lane_image = drawLane(frame.copy(), edges)

    blurred_edges = cv2.GaussianBlur(filtered_edges, (5, 5), 0)

    # Displaying the Canny edge detection and lane detection
    cv2.imshow('Canny Edge Video', blurred_edges)
    cv2.imshow('Lane Detection', lane_image)

    # Exit on pressing 'Esc'
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

src.release()
cv2.destroyAllWindows()