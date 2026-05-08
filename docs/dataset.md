Dataset consist of slef-recorded videos for training and evaluating hand gesture classification model. The project currently focuses on 4 classes:
- swipe up - 18 vid
- swipe down - 18 vid
- click - 9 vid
- none - 18 vid

Data collection
Dataset was collected using webcam recordings and processed frame-by-frame using OpenCV. Individual frames were passed MediaPipe Hands for landmark detection and extraction (2D coordinates). The depth coordinate (z) was excluded to reduce dimentionality and simplify the classification pipeline.

The dataset id not fully balanced across gesture classes. The "click" gesture contains fewer recordings because its motion pattern has a distinct landmark interaction, when 2 fingers connect, which makes it easier to sepeare it from remaining classes.

Limitations: small dataset
