// ----------------------------------------------------------------------------
//
// Copyright (C) 2023 Daniel Segal. All rights reserved.
// Use this source code "AS IS" with no warranty whatsoever
//
// $Author: daniilcg $
// $Rev: 450 $
// $Date: 2023-07-03 20:08:15 $
//
// ----------------------------------------------------------------------------

import cv2
import numpy as np

# Linearizes the color channels of an image
def linearize_image(image):
    # Create a copy of the image to avoid modifying the original
    linearized_image = image.copy().astype(np.float32) / 255.0

    # Linearize each color channel
    linearized_image = np.power(linearized_image, 2.2)

    # Convert back to the range [0, 255]
    linearized_image = (linearized_image * 255).astype(np.uint8)

    return linearized_image

# Load the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Failed to open the image file.")
    exit()

# Linearize the image
linearized_image = linearize_image(image)

# Save the linearized image
cv2.imwrite("output.jpg", linearized_image)

print("Linearization complete. Saved the output image.")
