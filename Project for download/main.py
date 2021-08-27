#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5.uic import loadUi
from urllib.request import urlretrieve
import re , wget, os, sys, pafy, humanize
import requests as r
from os import path
import urllib.request
from instaloader import Instaloader
from plyer import notification
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("untitled.ui",self)
        self.setWindowTitle("Anti Error Download")    # Set A Title For My App
        self.setWindowIcon(QIcon("icon/icon.ico"))    # Set A Icon For My App
        self.setWindowIconText("logo")
        self.setFont(QFont("Arial Black")) # Set A Font For My App
        self.selctionHome()
        self.homePage()
        self.filecontentWidget()
        self.videocontentWidget()
        self.listcontentWidget()
        self.facecontentWidget()
        self.settingcontentWidget()
        self.instacontentWidget()
        self.getVideo()
#==============================================================================#
    def homePage(self):
        self.downicon=self.findChild(QLabel , "label")
        self.downicon.setPixmap(QPixmap("photo/down.png"))
        self.powericon=self.findChild(QLabel , "label_4")
        self.powericon.setPixmap(QPixmap("photo/power.png"))
        self.settingicon=self.findChild(QLabel , "label_6")
        self.settingicon.setPixmap(QPixmap("photo/setting.png"))
        self.onevidicon=self.findChild(QLabel , "label_9")
        self.onevidicon.setPixmap(QPixmap("photo/youtube.png"))
        self.playlisticon=self.findChild(QLabel , "label_10")
        self.playlisticon.setPixmap(QPixmap("photo/list.png"))
        self.notifyicon=self.findChild(QLabel , "label_11")
        self.notifyicon.setPixmap(QPixmap("photo/notify.png"))
    def selctionHome(self):
        self.stackw=self.findChild(QStackedWidget , "stackedWidget")
        self.stackw.setCurrentIndex(0)
        self.homeBtn = self.findChild(QPushButton  , "pushButton")
        self.homeBtn.setIcon(QIcon("icon/home.ico"))
        self.homeBtn.clicked.connect(self.homeWidget)
        self.fileBtn = self.findChild(QPushButton  , "pushButton_2")
        self.fileBtn.setIcon(QIcon("icon/file.ico"))
        self.fileBtn.clicked.connect(self.fileWidget)
        self.videoBtn = self.findChild(QPushButton  , "pushButton_3")
        self.videoBtn.setIcon(QIcon("icon/youtubes.ico"))
        self.videoBtn.clicked.connect(self.videoWidget)
        self.listBtn = self.findChild(QPushButton  , "pushButton_6")
        self.listBtn.setIcon(QIcon("icon/playlist.ico"))
        self.listBtn.clicked.connect(self.listWidget)
        self.faceBtn = self.findChild(QPushButton  , "pushButton_7")
        self.faceBtn.setIcon(QIcon("icon/face.ico"))
        self.faceBtn.clicked.connect(self.facebookWidget)
        self.settingBtn = self.findChild(QPushButton  , "pushButton_15")
        self.settingBtn.setIcon(QIcon("icon/setting.ico"))
        self.settingBtn.clicked.connect(self.settingWidget)
        self.instaBtn = self.findChild(QPushButton  , "pushButton_16")
        self.instaBtn.setIcon(QIcon("icon/insta.ico"))
        self.instaBtn.clicked.connect(self.instaWidget)
    def homeWidget(self):
        self.stackw.setCurrentIndex(0)
    def fileWidget(self):
        self.stackw.setCurrentIndex(1)
    def videoWidget(self):
        self.stackw.setCurrentIndex(2)
    def listWidget(self):
        self.stackw.setCurrentIndex(3)
    def facebookWidget(self):
        self.stackw.setCurrentIndex(5)
    def settingWidget(self):
        self.stackw.setCurrentIndex(4)
    def instaWidget(self):
        self.stackw.setCurrentIndex(6)
#================================================================================#
    def filecontentWidget(self):
        self.pgbar = self.findChild(QProgressBar , "progressBar")
        self.pgbar.setValue(0)
        self.logofile = self.findChild(QLabel , "label_18")
        self.logofile.setPixmap(QPixmap("photo/files.png"))
        self.browseBtn=self.findChild(QPushButton , "pushButton_8")
        self.downBtn=self.findChild(QPushButton , "pushButton_5")
        self.downBtn.clicked.connect(self.downloadFile)
        self.browseBtn.setIcon(QIcon("photo/browse.png"))
        self.browseBtn.clicked.connect(self.locat)
        self.urldown=self.findChild(QLineEdit , "lineEdit")
        self.filepath=self.findChild(QLineEdit , "lineEdit_2")
    def videocontentWidget(self):
        self.logovideo=self.findChild(QLabel , "label_19")
        self.logovideo.setPixmap(QPixmap("photo/youtube2.png"))
        self.browseBtn1=self.findChild(QPushButton , "pushButton_9")
        self.browseBtn1.setIcon(QIcon("photo/browse.png"))
        self.urlvid = self.findChild(QLineEdit , "lineEdit_4")
        self.svlocat = self.findChild(QLineEdit , "lineEdit_3")
        self.browse = self.findChild(QPushButton , "pushButton_9")
        self.stdown = self.findChild(QPushButton , "pushButton_10")
        self.qualti = self.findChild(QComboBox , "comboBox")
        self.progress2=self.findChild(QProgressBar,"progressBar_2")
        self.progress2.setValue(0)
    def listcontentWidget(self):
        self.logolist=self.findChild(QLabel , "label_20")
        self.logolist.setPixmap(QPixmap("photo/youtubelist.png"))
        self.browseBtn2=self.findChild(QPushButton , "pushButton_11")
        self.browseBtn2.clicked.connect(self.locat3)
        self.browseBtn2.setIcon(QIcon("photo/browse.png"))
        self.urlList=self.findChild(QLineEdit,"lineEdit_6")
        self.pathList=self.findChild(QLineEdit,"lineEdit_5")
        self.downlist=self.findChild(QPushButton,"pushButton_12")
        self.downlist.clicked.connect(self.playlistGet)
    def facecontentWidget(self):
        self.logoface=self.findChild(QLabel , "label_22")
        self.logoface.setPixmap(QPixmap("photo/facelogo.png"))
        self.browseBtn3=self.findChild(QPushButton , "pushButton_14")
        self.browseBtn3.setIcon(QIcon("photo/browse.png"))
        self.browseBtn3.clicked.connect(self.locate4)
        self.urlfacedown=self.findChild(QLineEdit,"lineEdit_7")
        self.pathface=self.findChild(QLineEdit,'lineEdit_8')
        self.qualityFace=self.findChild(QComboBox,"comboBox_3")
        self.qualityFace.addItem("High Down")
        self.qualityFace.addItem("Low Down")
        self.downFaceBtn=self.findChild(QPushButton,"pushButton_13")
        self.downFaceBtn.clicked.connect(self.downFace)
    def settingcontentWidget(self):
        self.gotoFace=self.findChild(QLabel,"label_25")
        self.gotoFace.setText("<a href=\"www.facebook.com/faresemadx\">FACEBOOK</a>")
        self.gotoFace.setOpenExternalLinks(True)
        self.gotoTwitter=self.findChild(QLabel,"label_26")
        self.gotoTwitter.setText("<a href=\"www.twitter.com/faresemadx\">TWITTER</a>")
        self.gotoTwitter.setOpenExternalLinks(True)
        self.gotoInsta=self.findChild(QLabel,"label_27")
        self.gotoInsta.setText("<a href=\"www.instagram.com/farresemadd\">INSTAGRAM</a>")
        self.gotoInsta.setOpenExternalLinks(True)
        self.logoverified=self.findChild(QLabel , "label_21")
        self.logoProg = self.findChild(QLabel , "label_14")
        self.logoProg.setPixmap(QPixmap("photo/programmer.png"))
        self.logoverified.setPixmap(QPixmap("photo/logosetting2.jpg"))
    def instacontentWidget(self):
        self.logoinsta=self.findChild(QLabel , "label_23")
        self.logoinsta.setPixmap(QPixmap("photo/instalogo.png"))
        self.logoUser=self.findChild(QLabel,"label_29")
        self.logoUser.setPixmap(QPixmap("photo/human.png"))
        self.user=self.findChild(QLineEdit,"lineEdit_9")
        self.browseBtn4=self.findChild(QPushButton,"pushButton_17")
        self.browseBtn4.setIcon(QIcon("photo/browse.png"))
        self.browseBtn4.clicked.connect(self.locat5)
        self.pathInsta=self.findChild(QLineEdit,"lineEdit_10")
        self.downInsta=self.findChild(QPushButton,"pushButton_18")
        self.downInsta.clicked.connect(self.downInstascrape)
#================================================================================#
    def locat(self):
        save_place=QFileDialog.getExistingDirectory(self,"Select Download Directory")
        text = str(save_place)
        name=(text[0:].split(',')[0].replace("'",''))
        self.filepath.setText(name)
    def progress(self , block_num , block_size , total_size):
        data_recv = block_num * block_size
        prectage = (data_recv * 100) / total_size
        self.pgbar.setValue(int(prectage))
    def downloadFile(self):
        # chdir(self.filepath.text())
        url = self.url.text()
        file_name = url.split("/")[-1]
        urlretrieve(url ,f"{file_name}", self.progress)
        notification.notify(title="Download Succesfuly",message="The Download Finished",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\scorpion.ico",timeout=1)
#================================================================================#
    def getVideo(self):
        self.urlvid.editingFinished.connect(self.geturl)
        self.browse.clicked.connect(self.locate1)
        self.stdown.clicked.connect(self.downUrl)

    def locate1(self):
        save_place=QFileDialog.getExistingDirectory(self,"Select Download Directory")
        text = str(save_place)
        name=(text[0:].split(',')[0].replace("'",''))
        self.svlocat.setText(name)

    def geturl(self):
        video_link=self.urlvid.text()
        video=pafy.new(video_link)
        st=video.allstreams
        for s in st:
            size=humanize.naturalsize(s.get_filesize())
            data =f"{s.mediatype}  {s.extension}  {s.quality} {size}"
            self.qualti.addItem(data)

    def downUrl(self):
        try:
            video_link=self.urlvid.text()
            save_location=self.svlocat.text()
            video=pafy.new(video_link)
            st=video.allstreams
            quality=self.qualti.currentIndex()
            st[quality].download(filepath=save_location)
            self.urlvid.setText("")
            self.svlocat.setText("")
            notification.notify(title='Download', message='Download Succesfuly', app_name='Simple Download', app_icon='icon/youtube2.ico', timeout=4, ticker='fares', toast=False)
        except:
            pass
#================================================================================#
    def playlistGet(self):
        playlist_url=self.urlList.text()
        save_location=self.pathList.text()
        playlist=pafy.get_playlist(playlist_url)
        videos=playlist['items']
        os.chdir(save_location)
        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))
        for video in videos:
            p=video['pafy']
            best=p.getbest()
            best.download()
            self.urlList.setText("")
            self.pathList.setText("")
        notification.notify(title="Download Succesfuly",message="The Download PlayList Finished",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\scorpion.ico",timeout=1)
            
    def locat3(self):
        save_place=QFileDialog.getExistingDirectory(self,"Select Download Directory")
        text = str(save_place)
        name=(text[0:].split(',')[0].replace("'",''))
        self.pathList.setText(name)
    def locat5(self):
        save_place=QFileDialog.getExistingDirectory(self,"Select Download Directory")
        text = str(save_place)
        name=(text[0:].split(',')[0].replace("'",''))
        self.pathInsta.setText(name)
#================================================================================#
    def downFace(self):
        ERASE_LINE = '\x1b[2K'
        if self.qualityFace.currentText()=="Low Down":
            try:
                LINK = self.urlfacedown.text()
                html = r.get(LINK)
                sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
            except r.ConnectionError:
                notification.notify(title="ConnectionError",message="OOPS!! Connection Error.",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
            except r.Timeout:
                notification.notify(title="Timeout",message="OOPS!! Timeout Error.",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
            except r.RequestException:
                notification.notify(title="RequestException",message="OOPS!! General Error or Invalid URL",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
            except (KeyboardInterrupt, SystemExit):
                notification.notify(title="KeyboardInterrupt",message="Ok ok, quitting",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
                sys.exit(1)
            except TypeError:
                notification.notify(title="TypeError",message="Video May Private or Invalid URL",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
            else:
                sd_url = sdvideo_url.replace('sd_src:"', '')
                filedir=self.pathface.text()
                wget.download(sd_url, filedir)
                sys.stdout.write(ERASE_LINE)
                self.urlfacedown.setText("")
                self.pathface.setText("")
            notification.notify(title="Download Succesfuly",message="The Download Finished",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\scorpion.ico",timeout=1)
        elif self.qualityFace.currentText()=="High Down":
            try:
                LINK = self.urlfacedown.text()
                html = r.get(LINK)
                hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
            except r.ConnectionError:
                notification.notify(title="ConnectionError",message="OOPS!! Connection Error.",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
            except r.Timeout:
                notification.notify(title="Timeout",message="OOPS!! Timeout Error.",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
            except r.RequestException:
                notification.notify(title="RequestException",message="OOPS!! General Error or Invalid URL",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
            except (KeyboardInterrupt, SystemExit):
                notification.notify(title="KeyboardInterrupt",message="Ok ok, quitting",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
                sys.exit(1)
            except TypeError:
                notification.notify(title="TypeError",message="Video May Private or Invalid URL",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\icon.ico",timeout=4)
            else:
                hd_url = hdvideo_url.replace('hd_src:"', '')
                filedir=self.pathface.text()
                wget.download(hd_url, filedir)
                sys.stdout.write(ERASE_LINE)
                self.pathface.setText("")
                self.urlfacedown.setText("")
        notification.notify(title="Download Succesfuly",message="The Download Finished",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\scorpion.ico",timeout=1)
    def locate4(self):
        save_place=QFileDialog.getExistingDirectory(self,"Select Download Directory")
        text = str(save_place)
        name=(text[0:].split(',')[0].replace("'",''))
        self.pathface.setText(name)
    def downInstascrape(self):
        mode=Instaloader()
        username=self.user.text()
        os.chdir(self.pathInsta.text())
        mode.download_profile(username,profile_pic_only=True)
        notification.notify(title="Download Succesfuly",message="The Download Finished",app_name="Scorpion Download",app_icon="C:\\Users\\Scorpion\\Desktop\\testststs\\icon\\scorpion.ico",timeout=1)
#================================================================================#

def run():
    try:
        app=QApplication(argv)
        myapp=Mainwindow()
        myapp.show()
        app.exec_()
    except Exception as error:
        print(error)
if __name__ == "__main__":
    run()