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
This is an utility module for the main project which include functions to judge the posture of a person using coordinates of appropriate joints.
"""
import math
import numpy as np
import logging

__author__: str = "Maithil Saha"
__date__: str = "2023-09-28"
__purpose__: str = "Posture analysis using coordinates of body parts."
__metadata__: tuple[str, ...] = None


# Configure the logging module
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO


def calculate_distance(
    point1: tuple[float, float], point2: tuple[float, float]
) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        point1 (tuple): A tuple (x, y) representing the first point.
        point2 (tuple): A tuple (x, y) representing the second point.

    Returns:
        float: The Euclidean distance between the two points.

    Mathematics:
    The Euclidean distance between two points (x1, y1) and (x2, y2) is calculated as:
    distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

    Time Complexity:
    O(1) - Constant time, as it involves basic arithmetic operations.

    Space Complexity:
    O(1) - Constant space, as it only stores the result.
    """
    x1: float
    y1: float
    x2: float
    y2: float

    x1, y1 = point1
    x2, y2 = point2
    dx: float = x2 - x1
    dy: float = y2 - y1
    distance: float = np.sqrt(dx**2 + dy**2)
    return distance


# Define other functions with minimal computation as needed...


def isPosture_good(
    left_shoulder: tuple[float, float],
    right_shoulder: tuple[float, float],
    # Uncomment if used
    # right_hip: tuple[float, float],
    # left_hip: tuple[float, float],
    # left_elbow: tuple[float, float],
    # right_elbow: tuple[float, float],
    nose: tuple[float, float],
    # eyes: tuple[float, float],
    # lips: tuple[float, float],
) -> bool:
    """
    Main function to check overall posture.

    Args:
        left_shoulder (tuple): A tuple (x, y) representing the left shoulder.
        right_shoulder (tuple): A tuple (x, y) representing the right shoulder.
        right_hip (tuple): A tuple (x, y) representing the right hip.
        left_hip (tuple): A tuple (x, y) representing the left hip.
        left_elbow (tuple): A tuple (x, y) representing the left elbow.
        right_elbow (tuple): A tuple (x, y) representing the right elbow.
        nose (tuple): A tuple (x, y) representing the nose.
        eyes (tuple): A tuple (x, y) representing the eyes.
        lips (tuple): A tuple (x, y) representing the lips.

    Returns:
        bool: True if the posture is good, False if the posture is bad.

    Mathematics:
    This function evaluates the overall posture based on several criteria, such as the distance between shoulders and hips.
    Additional criteria can be added as needed for a more comprehensive analysis.

    Time Complexity:
    O(1) - The time complexity depends on the number of conditions checked, which is typically constant.

    Space Complexity:
    O(1) - The space complexity is constant as it does not depend on the input size.

    Possible Errors and How to Address Them:
    - Input coordinates may be missing or invalid (e.g., not tuples of floats).
      - Address by ensuring that valid coordinate tuples are provided as input.
    - The distance threshold for good posture may not be appropriate for all cases.
      - Adjust the distance thresholds based on specific posture criteria.
    """
    # Calculate only what's needed for posture evaluation
    shoulder_distance: float = calculate_distance(left_shoulder, right_shoulder)
    shoulder_tilt: float = abs(
        math.degrees(
            math.atan2(
                right_shoulder[1] - left_shoulder[1],
                right_shoulder[0] - left_shoulder[0],
            )
        )
    )
    shoulder_to_nose_distance = calculate_distance(nose, left_shoulder)

    # Definng conditions:
    condition1 = 0.45 > shoulder_distance > 0.35  # Adjustable threshold
    condition2 = shoulder_tilt >= 178  # Adjustable threshold
    condition3 = shoulder_to_nose_distance > 0.35  # Adjustable threshold
    # Taking intersection of all conditions
    is_good_posture: bool = condition1 and condition2 and condition3

    # Log the posture result
    """if is_good_posture:  # Uncomment for debugging
        logging.info("Posture is GOOD")
    else:
        logging.info("Posture is BAD")
    """
    return (
        is_good_posture,
        [shoulder_distance, condition1],
        [shoulder_tilt, condition2],
        [shoulder_to_nose_distance, condition3],
    )


# Example usage:
if __name__ == "__main__":
    logging.info(__metadata__)
    logging.warning(
        "This is a utility module to the the main project. Do not execute this as a script."
    )
