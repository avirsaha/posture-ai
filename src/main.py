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
"""
This is the main script of the project. Execute this for running the program.
"""

# Metadata
__title__: str = "sitfix-ai"
__description__: str = """A Python project for demonstrating the use of computer vision 
                          in maintaning healthy posuture while working on a computer."""
__version__: str = "0.1.0-alpha"
__authors__: tuple[str, ...] = ("Aviraj Saha",)
__authors_email__: tuple[str, ...] = ("your@email.com",)
__license__: str = "MIT License"
__url__: str = "https://github.com/avirsaha/sitfix-ai"
__dependencies__: tuple[str, ...] = (
    "absl-py==2.0.0"
    "attrs==23.1.0"
    "cffi==1.15.1"
    "contourpy==1.1.1"
    "cycler==0.11.0"
    "flatbuffers==23.5.26"
    "fonttools==4.42.1"
    "kiwisolver==1.4.5"
    "matplotlib==3.8.0"
    "mediapipe==0.10.5"
    "numpy==1.26.0"
    "opencv-contrib-python==4.8.0.76"
    "packaging==23.1"
    "Pillow==10.0.1"
    "protobuf==3.20.3"
    "pycparser==2.21"
    "pyparsing==3.1.1"
    "python-dateutil==2.8.2"
    "six==1.16.0"
    "sounddevice==0.4.6"
)
__keywords__: tuple[str, ...] = tuple()

__metadata__: tuple[str | tuple, ...] = (
    __title__,
    __description__,
    __version__,
    __authors__,
    __authors_email__,
    __license__,
    __url__,
    __dependencies__,
    __keywords__,
)

# Importing dependencies
import math
import cv2
import mediapipe as mp
from typing import Final
from logging import basicConfig, error, ERROR
import judge
import winsound

# Configure logging to show only errors
basicConfig(level=ERROR)


def initialize_pose_model() -> mp.solutions.pose.Pose | None:
    """
    Initialize and configure the MediaPipe pose model.

    Returns:
        mp.solutions.pose.Pose: Initialized pose model.

    Author: Aviraj Saha
    Date: September 30, 2023
    Purpose: Initialize the pose detection model for detecting human poses.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    try:
        # Define the MediaPipe pose model
        MEDIAPIPE_POSE_MODEL: Final[mp.solutions.pose] = mp.solutions.pose
        # Initialize the pose model with confidence thresholds
        pose: Final[mp.solutions.pose.Pose] = MEDIAPIPE_POSE_MODEL.Pose(
            min_detection_confidence=0.9, min_tracking_confidence=0.9
        )
        return pose
    except Exception as e:
        error(f"Error initializing pose model: {e}")
        return None


def capture_video(camera_index: int) -> cv2.VideoCapture | None:
    """
    Capture video from the camera.

    Args:
        camera_index (int): Index of the camera to capture video from.

    Returns:
        cv2.VideoCapture: Video capture object.

    Author: Aviraj Saha
    Date: September 28, 2023
    Purpose: Initialize video capture from the specified camera.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    try:
        # Create a video capture object for the specified camera
        CAPTURE: Final[cv2.VideoCapture] = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        return CAPTURE
    except Exception as e:
        error(f"Error capturing video: {e}")
        return None


def process_frame(
    frame: cv2.typing.MatLike, pose: mp.solutions.pose.Pose
) -> tuple[cv2.typing.MatLike, object] | tuple[None, None]:
    """
    Process a video frame, detect and visualize human poses.

    Args:
        frame (object): Video frame to process.
        pose (mp.solutions.pose.Pose): Initialized pose model.

    Returns:
        Tuple[object, object]: Processed image and pose detection results.

    Author: Aviraj Saha
    Date: September 28, 2023
    Purpose: Process a video frame for pose detection.
    Time Complexity: Depends on the image size and pose detection model.
    Space Complexity: Depends on the image size and pose detection model.
    """
    try:
        final_width: int = 1280  # Alterable
        final_height: int = 960  # Alterable

        # Resize the frame to a specific width and height
        frame: cv2.typing.MatLike = cv2.resize(frame, (final_width, final_height))
        # Convert frame colors from BGR to RGB
        image: cv2.typing.MatLike = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Process the frame using the pose model
        results: object = pose.process(image)

        # Convert image colors back from RGB to BGR
        image.flags.writeable = True
        image: cv2.typing.MatLike = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        return image, results
    except Exception as e:
        error(f"Error processing frame: {e}")
        return None, None


def display_posture_status(
    image: cv2.typing.MatLike, posture_status: bool, *cases: list[tuple[float, bool]]
) -> None:
    """
    Display posture status on the image.

    Args:
        image (object): Image to display on.
        posture_status (bool): Whether the posture is good or not.
        angle (float): Angle related to the posture.

    Author: Aviraj Saha
    Date: September 30, 2023
    Purpose: Display posture status on the processed image.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    try:
        # Display posture status as text on the image
        if not posture_status:
            winsound.Beep(800, 10)
            cv2.putText(
                image,
                "Poor Posture",
                (80, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 255),
                2,
            )

        else:
            cv2.putText(
                image,
                "Good posture",
                (80, 80),
                cv2.FONT_HERSHEY_COMPLEX,
                3,
                (255, 0, 0),
                2,
            )
        inc: int = 0
        for item in cases:
            inc += 50
            colors: tuple[int] = (255, 0, 0)
            if not item[1]:
                colors = (0, 0, 255)
            cv2.putText(
                image,
                f"{math.floor(item[0])}",
                (1200, 80 + inc),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                colors,
                2,
            )

    except Exception as e:
        error(f"Error displaying posture status: {e}")


def process_video(pose: mp.solutions.pose.Pose, camera_index: int) -> None:
    """
    Process video frames, detect posture, and visualize it.

    Args:
        pose (mp.solutions.pose.Pose): Initialized pose model.
        camera_index (int): Index of the camera to capture video from.

    Author: Aviraj Saha
    Date: September 30, 2023
    Purpose: Continuously process video frames for posture detection and visualization.
    Time Complexity: Depends on the frame rate and image size.
    Space Complexity: Depends on the frame rate and image size.
    """
    try:
        # Create a video capture object
        CAPTURE: Final[cv2.VideoCapture] = capture_video(camera_index)

        while CAPTURE.isOpened():
            try:
                _: bool
                frame: cv2.typing.MatLike
                _, frame = CAPTURE.read()

                # Process the video frame and get results
                image: cv2.typing.MatLike
                results: object
                image, results = process_frame(frame, pose)
                if results:
                    if results.pose_landmarks:
                        left_shoulder: object = results.pose_landmarks.landmark[
                            mp.solutions.pose.PoseLandmark.LEFT_SHOULDER
                        ]
                        right_shoulder: object = results.pose_landmarks.landmark[
                            mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER
                        ]
                        right_hip: object = results.pose_landmarks.landmark[
                            mp.solutions.pose.PoseLandmark.RIGHT_HIP
                        ]
                        left_hip: object = results.pose_landmarks.landmark[
                            mp.solutions.pose.PoseLandmark.LEFT_HIP
                        ]
                        nose: object = results.pose_landmarks.landmark[
                            mp.solutions.pose.PoseLandmark.NOSE
                        ]
                        posture_status: bool
                        (
                            posture_status,
                            shoulder_distance,
                            shoulder_tilt,
                            shoulder_to_nose_distance,
                        ) = judge.isPosture_good(
                            left_shoulder=(left_shoulder.x, left_shoulder.y),
                            right_shoulder=(
                                right_shoulder.x,
                                right_shoulder.y,
                            ),
                            nose=(nose.x, nose.y),
                        )
                        # Display the posture status on the image

                        # shoulder_distance = str(float(shoulder_distance) * 100)
                        # shoulder_tilt = str(180 - float(shoulder_tilt))
                        # shoulder_to_nose_distance = str(
                        #     float(shoulder_to_nose_distance) * 100
                        # )
                        shoulder_distance[0] *= 100
                        shoulder_to_nose_distance[0] *= 100
                        shoulder_tilt[0] = 180 - shoulder_tilt[0]
                        display_posture_status(
                            image,
                            posture_status,
                            shoulder_distance,
                            shoulder_tilt,
                            shoulder_to_nose_distance,
                        )

                else:
                    error("No human figure detected")

                # Draw landmarks on the frame
                mp.solutions.drawing_utils.draw_landmarks(
                    image, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS
                )

                cv2.putText(
                    image,
                    "Stats",
                    (1100, 50),
                    cv2.FONT_HERSHEY_COMPLEX,
                    2,
                    (255, 0, 0),
                    2,
                )

                cv2.putText(
                    image,
                    "Head:",
                    (950, 130),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (255, 0, 0),
                    2,
                )

                cv2.putText(
                    image,
                    "Shoulder:",
                    (950, 180),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (255, 0, 0),
                    2,
                )

                cv2.putText(
                    image,
                    "Body:",
                    (950, 230),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (255, 0, 0),
                    2,
                )

                # Show the final frame
                cv2.imshow("sitfix-ai Visual Output", image)

                if cv2.waitKey(10) & 0xFF == ord("q"):
                    break

            except Exception as e:
                error(f"Error in video processing loop: {e}")

        CAPTURE.release()
        cv2.destroyAllWindows()

    except Exception as e:
        error(f"Error in process_video function: {e}")


def main() -> None:
    """
    Execution starts from here.

    Args:
        pose (mp.solutions.pose.Pose): Initialized pose model.
        camera_index (int): Index of the camera to capture video from.

    Author: Aviraj Saha
    Date: September 28, 2023

    Purpose: This is the main scope of the function.
    Time Complexity: Depends on the other functions.
    Space Complexity: Depends on the other functions.
    """
    try:
        # Initialize the pose model
        pose: mp.solutions.pose.Pose = initialize_pose_model()
        if pose is not None:
            # Process video frames for posture detection
            process_video(pose, camera_index=0)
    except Exception as e:
        error(f"Error in main function: {e}")


if __name__ == "__main__":
    # print(__metadata__)  # Uncomment for printing metadata attached to this code.
    main()
