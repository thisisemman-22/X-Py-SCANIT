import cv2
import numpy as np
from pyzbar.pyzbar import decode

def scan_barcode():
    """Scan barcodes and return the scanned barcode data."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return {"error": "Could not open video capture."}

    barcode_data = None
    try:
        while True:
            # Read frame from camera
            ret, frame = cap.read()
            if not ret:
                return {"error": "Could not read frame."}

            # Decode barcodes in the frame
            decoded_objects = decode(frame)

            for obj in decoded_objects:
                # Filter out PDF417 barcodes if not needed
                if obj.type == 'PDF417':
                    continue

                # Draw a rectangle around detected barcode
                points = obj.polygon
                if len(points) == 4:  # Only process rectangular barcodes
                    pts = [(point.x, point.y) for point in points]
                    cv2.polylines(frame, [np.array(pts, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)

                    # Display the decoded data
                    barcode_data = obj.data.decode('utf-8')

                    cv2.putText(frame, barcode_data, (pts[0][0], pts[0][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # Show the frame with detected barcodes
            cv2.imshow("Barcode Scanner", frame)

            # Break the loop on 'q' key press or if a barcode is detected
            if cv2.waitKey(1) & 0xFF == ord('q') or barcode_data:
                break
    finally:
        # Release the camera and close windows
        cap.release()
        cv2.destroyAllWindows()

    return barcode_data if barcode_data else {"error": "No barcode detected."}
