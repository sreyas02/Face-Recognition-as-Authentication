# face-recognition-as-authentication

Face recognition as authentication

Here we will replace our OTP by face recognition technology. We will recognize if the user who is making the transaction is legit or not by replacing one time passwords so as we will decrease the time of transaction and make it more secure.

We started with openCV library in python for recognizing faces of users because OpenCV provides a huge suite of algorithms and aims at real-time computer vision .Project works in three parts which will be explained in detailed.

Initially user have to register his/her face by clicking register button web cam will open and it will take the 100 snaps of user within seconds and then those data will be trained by LBPH face recognizer we used this algorithm because it will train data very fast and when our data is trained then lastly when user want to login webcam will open and if the model has 75 percent confidence then it will move to further operations otherwise it shows invalid user. We integrated this model to frontend by using tkinter framework python's standard GUI. So we can see this model working by just pressing the buttons provided.
