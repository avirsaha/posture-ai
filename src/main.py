# MIT License
# Copyright (c) 2023 The_BDMI_Students_Exhibition_Team_2023
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import cv2
import mediapipe as mp
from typing import Final
from logging import basicConfig, error, ERROR

# Configure logging to show only errors
basicConfig(level=ERROR)


def main() -> None:
    """
    This function initializes the pose model, captures video, and processes it to detect and visualize human poses.
    """

    # Initialization for mediapipe pose model and drawing_utils for visuals
    MEDIAPIPE_RENDERER: Final[object] = mp.solutions.drawing_utils
    MEDIAPIPE_POSE_MODEL: Final[object] = mp.solutions.pose

    # Create a capture object to access the camera
    CAPTURE: Final[object] = cv2.VideoCapture(
        0, cv2.CAP_DSHOW
    )  # Change the camera index if needed, and use CAP_DSHOW for Windows

    # Custom image size
    final_width: int = 1280  # Width of the final frame
    final_height: int = 960  # Height of the final frame

    # Setup Mediapipe pose instance
    with MEDIAPIPE_POSE_MODEL.Pose(
        min_detection_confidence=0.5, min_tracking_confidence=0.5
    ) as pose:
        # Video capture and display loop
        while CAPTURE.isOpened():
            try:
                # Read a frame from the camera
                _, frame = CAPTURE.read()

                # Resize the frame
                frame = cv2.resize(frame, (final_width, final_height))

                # Pose detection and visuals

                # Recolor from BGR to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Saving results from pose model
                results = pose.process(image)

                # Recolor from RGB to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Draw landmarks on the frame
                MEDIAPIPE_RENDERER.draw_landmarks(
                    image, results.pose_landmarks, MEDIAPIPE_POSE_MODEL.POSE_CONNECTIONS
                )

                # Show the final frame
                cv2.imshow("sitfix-ai Visual Output", image)

                # Press 'q' to exit the loop and close the visual window
                if cv2.waitKey(10) & 0xFF == ord("q"):
                    break

            except Exception as e:
                # Log any exceptions that occur during processing
                error(e)

        # Release the camera and close all OpenCV windows
        CAPTURE.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
