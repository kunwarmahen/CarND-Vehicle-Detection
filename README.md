##Vehicle Detection Project


[//]: # (Image References)
[image1]: ./output_images/output_6_1.png
[image2]: ./output_images/output_6_2.png
[image5]: ./output_images/output_7_1.png
[image6]: ./output_images/output_7_2.png
[image7]: ./output_images/output_7_3.png
[image8]: ./output_images/output_7_4.png
[image9]: ./output_images/output_7_5.png
[image10]: ./output_images/output_7_6.png
[image11]: ./output_images/output_7_7.png
[video1]: ./output_images/output.mp4

## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points
###Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
###Histogram of Oriented Gradients (HOG)

####1. Explain how (and identify where in your code) you extracted HOG features from the training images.

The code for this step is contained in the function get_hog_features in third code cell of the IPython notebook.  

I started by reading in all the `vehicle` and `non-vehicle` images under train function.   Here is an example of one of each of the `vehicle` and `non-vehicle` classes:

![alt text][image1]

I then explored different color spaces and different `skimage.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two classes and displayed them to get a feel for what the `skimage.hog()` output looks like.

Here is an example using the `YCrCb` color space and HOG parameters of `orientations=9`, `pixels_per_cell=(8, 8)` and `cells_per_block=(2, 2)`:


![alt text][image2]

####2. Explain how you settled on your final choice of HOG parameters.

I tried various combinations of parameters but settled with above values for the parameter. Most important was selecting color space YCrCb. 

####3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

As part of training I calculated hog_feature and also calculated spatial_feature and histogram features. Combined all the features and then applied normalization to the combined value. I took these normalized result and split them into 80 is to 20 ratio for training vs test data. I then trained a linear SVM using the test data from previous step. I then calculated the test accuracy. Test accuracy came to 99.32%.

###Sliding Window Search

####1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

Next I implemented the logic to search for vehicles in the test frame using sliding window technique using window sizes of (32 x 32) (64 x 64) and (128 x 128) which helped me find cars far away in the frame and close by as well.

####2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

Ultimately I searched on scale of 1.5 using YCrCb 3-channel HOG features plus spatially binned color and histograms of color in the feature vector, which provided a nice result.  Here are example image, right most is the output which shows all the different blocks where it thinks a vehicle is present.

![alt text][image5]
---

### Video Implementation

####1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
Here's a [link to my video result](./output_images/output.mp4)

Here is the link for video result which was sampled across 10 frames to see if the car is still there or was it a false positive.[link to my video result with sampling](./output_images/output_with_sampling.mp4)



####2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.  

Here's an example result showing the heatmap on test images and the bounding boxes then overlaid:

![alt text][image5]
![alt text][image6]
![alt text][image7]
![alt text][image8]
![alt text][image9]
![alt text][image10]
![alt text][image11]




---

###Discussion

####1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

While implementing the solution biggest challenges I faced were around how to remove remove false positives. I had tried to implement a solution where it takes a look at 10 frames and check if the box is roughly around the same place for at least 3 times. This helped removing most of the false positives but it also had scenarios where it removes bounding boxes around identified car. This is something I need to work further.
