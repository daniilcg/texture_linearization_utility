# texture_linearization_utility
In this example, we're using the OpenCV library to handle image I/O and manipulation. The linearize_image function takes an input image, converts it to a floating-point representation in the range [0, 1], applies the linearization transformation (raising to the power of 2.2), and then scales it back to the range [0, 255] as an unsigned 8-bit integer.

You can adjust the linearize_image function to support other color spaces, such as DCI P3, by adding the necessary transformations as described in the utility. Remember to ensure that you have OpenCV installed in your Python environment before running this code.
