from sklearn.externals import joblib

# saving models/classifiers
clf.fit(x_train, y_train)
filename = "saved model.sav"
joblib.dump(clf, filename)

# openning models
clf = joblib.load(filename)
