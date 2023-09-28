# Project Name Documentation

Author: [Aviraj Saha](mailto:aviraj.saha@outlook.com)

## Table of Contents

- [Dependencies](#dependencies)
- [License](#license)
- [How to Contribute](#how-to-contribute)
- [Working Principle of Functions](#working-principle-of-functions)
  - [initialize_pose_model](#initialize_pose_model)
  - [capture_video](#capture_video)
  - [process_frame](#process_frame)
  - [display_posture_status](#display_posture_status)
  - [process_video](#process_video)
- [Time and Space Complexity](#time-and-space-complexity)
- [Environment Setup](#environment-setup)
- [Code of Conduct](#code-of-conduct)

## Dependencies

- [Python](https://www.python.org/) (>= 3.10)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## How to Contribute

We welcome contributions! Please follow our [contribution guidelines](CONTRIBUTING.md).

## Working Principle of Functions

### `initialize_pose_model`

This function initializes and configures the MediaPipe pose model for detecting human poses.

*Time Complexity*: O(1)
*Space Complexity*: O(1)

### `capture_video`

This function captures video from the camera specified by the `camera_index`.

*Time Complexity*: O(1)
*Space Complexity*: O(1)

### `process_frame`

This function processes a video frame, detecting and visualizing human poses.

*Time Complexity*: Depends on the image size and pose detection model.
*Space Complexity*: Depends on the image size and pose detection model.

### `display_posture_status`

This function displays posture status on the provided image.

*Time Complexity*: O(1)
*Space Complexity*: O(1)

### `process_video`

This function continuously processes video frames for posture detection and visualization.

*Time Complexity*: Depends on the frame rate and image size.
*Space Complexity*: Depends on the frame rate and image size.

## Time and Space Complexity

Here, we summarize the time and space complexities of each function.

| Function               | Time Complexity           | Space Complexity         |
|------------------------|---------------------------|--------------------------|
| `initialize_pose_model`| O(1)                      | O(1)                     |
| `capture_video`        | O(1)                      | O(1)                     |
| `process_frame`        | Depends on image size and model | Depends on image size and model |
| `display_posture_status`| O(1)                     | O(1)                     |
| `process_video`        | Depends on frame rate and image size | Depends on frame rate and image size |

## Environment Setup

To set up the environment for running this program, follow these steps:

1. Clone the repository: `git clone https://github.com/avirsaha/sitfix-ai.git`
2. Install Python (>= 3.7) from [python.org](https://www.python.org/).
3. Install dependencies: `pip install -r requirements.txt`

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a respectful and inclusive community.