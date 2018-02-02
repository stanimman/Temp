# Use the validation set to tune hyperparameters (regularization strength and
# learning rate). You should experiment with different ranges for the learning
# rates and regularization strengths; if you are careful you should be able to
# get a classification accuracy of about 0.4 on the validation set.

learning_rates = [9e-8, 1e-7, 2e-7, 3e-7]
regularization_strengths = [5e4, 4e4, 3e4, 2e4]

# results is dictionary mapping tuples of the form
# (learning_rate, regularization_strength) to tuples of the form
# (training_accuracy, validation_accuracy). The accuracy is simply the fraction
# of data points that are correctly classified.

results = {}
best_val = -1   # The highest validation accuracy that we have seen so far.
best_svm = None # The LinearSVM object that achieved the highest validation rate.

################################################################################
# TODO:                                                                        #
# Write code that chooses the best hyperparameters by tuning on the validation #
# set. For each combination of hyperparameters, train a linear SVM on the      #
# training set, compute its accuracy on the training and validation sets, and  #
# store these numbers in the results dictionary. In addition, store the best   #
# validation accuracy in best_val and the LinearSVM object that achieves this  #
# accuracy in best_svm.                                                        #
#                                                                              #
# Hint: You should use a small value for num_iters as you develop your         #
# validation code so that the SVMs don't take much time to train; once you are #
# confident that your validation code works, you should rerun the validation   #
# code with a larger value for num_iters.                                      #
################################################################################

for i in xrange(learning_rates.shape):
	for j in xrange (regularization_strength.shape):

	svm = LinearSVM()
	loss_hist = svm.train(X_train, y_train, i, reg=j
                      num_iters=1500, verbose=True)
					  
	y_val_pred = svm.predict(X_val)
	y_train_pred = svm.predict(X_train)
	
	Val_accuracy = (np.mean(y_val == y_val_pred), )
	Train_accuracy = (np.mean(y_train == y_train_pred), )
	
	if j == 0
		best_val = accuracy
		best_svm = svm 
		result {[learning_rate[i], regularization_strength[j]]:[y_train_pred,y_val_pred]}
	
	if best_val < accuracy
		best_val = accuracy
		best_svm = svm 
	results {[i,j]]:[Train_accuracy,Val_accuracy]}
