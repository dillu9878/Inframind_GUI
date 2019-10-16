
# import system module
import sys
import time
import os
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


# import Opencv module
import cv2


from ui_main_window import *
#from resultwidgetfinal import *

class CamMainWindow(QWidget):

    def cancel(self):
        '''
        f = open('flag.txt', 'r')
        s = f.read()
        f.close()
        s = int(s.strip())

        f = open('flag.txt', 'w')
        f.write(str(max(0, s - 1)))
        f.close()
        '''
        self.close()

    # class constructor
    def __init__(self):
        # call QWidget constructor

        super().__init__()
        self.ui = Ui_Form_Cam()
        self.ui.setupUi(self)
        self.setGeometry(-170, -100, 680, 500)


        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        #self.viewCam
        # set control_bt callback clicked  function
        self.controlTimer()
        self.ui.control_bt.clicked.connect(self.controlTimer)

        #self.ui.control_bt1.clicked.connect(self.cancel)

    # view camera
    def result(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form_R(self.Form)
        self.Form.show()
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        r = 300.0 / image.shape[1]
        #int(image.shape[0] * r)
        dim = (680, 500 )
        im = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        #print(image.shape,im.shape)
        image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if  self.timer.isActive():
        	# stop timer
            self.timer.stop()
            t,img=self.cap.read()
            # release video capture
            self.cap.release()
            time.sleep(1)
            buttonReply = QMessageBox.question(self, 'cam', "Image is clear or not?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply==QMessageBox.Yes:
                l=os.listdir('./Image/')
                l1 = os.listdir(f'./Image/customer_id:{len(l)}/')
                cv2.imwrite('./Image/customer_id:{}/input{}.jpeg'.format(len(l), len(l1) + 1 ),img)
                #cv2.destroyAllWindow()
                #time.sleep(1)
                self.close()
                #return 0
                #self.result()

            # update control_bt text
            else:
                self.ui.control_bt.setText("Capture")
                self.cap = cv2.VideoCapture(0)
                # start timer
                self.timer.start(20)
        	
        # if timer is started
        else:
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            #self.ui.control_bt.setText("Capture")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = CamMainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
