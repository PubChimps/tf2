n_input = 784  
n_classes = 10  
dropout = 1  
num_epochs = 40

X = tf.placeholder(tf.float32, [n_input, None])
Y = tf.placeholder(tf.float32, [n_classes, None])
W1 = tf.get_variable("W1", [64,n_input], initializer = tf.random_normal_initializer)
b1 = tf.get_variable("b1", [64,1], initializer = tf.zeros_initializer())
W2 = tf.get_variable("W2", [32,64], initializer = tf.random_normal_initializer)
b2 = tf.get_variable("b2", [32,1], initializer = tf.zeros_initializer())
W3 = tf.get_variable("W3", [10,32], initializer = tf.random_normal_initializer)
b3 = tf.get_variable("b3", [10,1], initializer = tf.zeros_initializer())

Z1 = tf.add(tf.matmul(W1,X), b1)                      
A1 = tf.nn.relu(Z1)                                   
Z2 = tf.add(tf.matmul(W2,A1), b2) 
A2 = tf.nn.relu(Z2) 
Z3 = tf.add(tf.matmul(W3,A2), b3) 

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=tf.transpose(Z3), labels=tf.transpose(Y)))

optimizer = tf.train.AdamOptimizer(learning_rate=.01).minimize(cost)
init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    for epoch in range(num_epochs):
        _ , epoch_cost = sess.run([optimizer, cost], feed_dict={X: X_train, Y: Y_train})
        if epoch % 20 == 0:
            print ("Cost after epoch %i: %f" % (epoch, epoch_cost))
        
 

    correct_prediction = tf.equal(tf.argmax(Z3), tf.argmax(Y))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print ("Train Accuracy:", accuracy.eval({X: X_train, Y: Y_train}))
