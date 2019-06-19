# IBM Watson Studio and TensorFlow 2.0

TensorFlow 2.0 just had its beta release a couple days ago. This major release focuses on community, simplicity, and ease of use, so I wanted to show the IBM Data Science Community how it can be used on IBM's Data Science Platform, Watson Studio.

First, we can see an example of a network built and trained in TensorFlow 1.X. Here we can see the presence of TensorFlow placeholders and TensorFlow Sessions, hallmarks of TF 1.X models. These are used by TensorFlow in order to build a computational graph before it is executed so that a model can be be optimized in a faster programming language like C++ or CUDA and distributed across a cluster.
<img src="images/tf1.png">

The following code is used to update TensorFlow in Watson Studio. You can download a notebook [here](https://github.com/PubChimps/tf2/blob/master/tf2wswalkthrough.ipynb) to follow along in Watson Studio. 
<img src="images/tf2install.png">

Next, TensorFlow's new upgrade utility allows for the automatic conversion of TensorFlow 1.X code into TensorFlow 2.0 code. It can be used on the previous network shown as follows.
<img src="images/nbscripting.png">

The rest of the notebook shows how to build the same network in Keras, which as of TensorFlow 2.0 is the the high-level API for TensorFlow. The network can be trained using two different methods, both of which are shown.

If you have any questions about this post or the accompanying notebook contact IBM Developer Advocate Nick Acosta at nacosta@us.ibm.com. To keep up on all things TensorFlow 2.0 check out their [website](https://www.tensorflow.org/beta) (of which many of the examples discussed here are derived from) and [Medium](https://medium.com/tensorflow), and be sure to attend the [TensorFlow meetup sponsored by the IBM Data Science Community June 27th in San Francisco](https://www.meetup.com/Advanced-Spark-and-TensorFlow-Meetup/events/261787740/).
