![Lowes](https://i.ibb.co/5YyzjrQ/lowes.png)

# 5152 Lowes Product Detection


Lowes has asked us to attempt to detect and classify products in their aisles.  This is part of a problem they are facing where they will need to detect products that are either on the shelf, or not on the shelf.  For this part of our project, we focused on classifying objects that are on the shelf. This would help Lowes along the path of training a model, or a variety of models, to recognize whether or not a product is out of stock.  

For our project, we trained Tiny YOLO to detect and classify products on Lowes store shelves.  We visited Lowes, collected training data from high resolution videos taken via our smartphones, and then trained YOLOv3 to recognize the products that were on the shelves. 

This project was implemented in Python using an open source repository called darknet, which is a Python YOLOv3 wrapper.  We trained the model using the Tiny YOLO weights, which is a much smaller model used for constrained environments.  

Information on YOLOv3 and darknet can be found at these locations: 

https://github.com/madhawav/YOLO3-4-Py

https://pjreddie.com/darknet/yolo/

Here is an example of what the YOLO network looks lik, taken from the author's academic paper: 

![YOLO](https://i.ibb.co/XFNf2vY/yolo.png)


Using this model, darknet was implemented with our training data.  The training videos taken from our smartphones were split using OpenCV 2, then labeled individually using LabelMe.  500 images were labeled with their respective classes for the multiclass model that was built, then the modeled was trained to minimize loss between the predictions and the correct lables.

Loss Function:

![Loss](https://i.ibb.co/f2JCPkC/loss-function.png)

Our labels were then applied to the predicted class bounding boxes, resulting in images that look similar to the below image.  This is the most likely predicted class with its corresponding probability:

![Labeled Products](https://i.ibb.co/Ld0hhv9/products2.png)

This is an example of a multi-class approach.  In reality, it would also be possible to train this model to recognize generalizable classes like detergent, axes, pesticide, etc.  Images having these classes would then be extracted from their bounding boxes using the corresponding coordinates, then fed into a feature detector/image search algorithm that could detect the similarity between these images and the corresponding Lowes product. 

Lowes has provided us with their catalog images and their corresponding names based on their online catalog.  This dataset could be used as the search dataset for input into a SIFT-like similarity detector.  An index could be created based on similarity that would match an extracted image with its corresponding product. 
