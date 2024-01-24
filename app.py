<<<<<<< HEAD

from flask import Flask,request
from flask import Flask, render_template,request
import tensorflow as tf
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def main():
    model=tf.keras.models.load_model("brain_tumor_network.h5")
    try:
        if request.method=='POST':
            data = request.json
            a=data["img"]
            bytes_decoded=base64.b64decode(a)
            img=Image.open(BytesIO(bytes_decoded))
            img=img.convert('RGB')
            img.save('test.jpg')
            img=cv2.imread('test.jpg')
            img=cv2.resize(img,dsize=(256,256),interpolation=cv2.INTER_CUBIC)
            img=img/255
            image=np.array([img])
            pred=model.predict(image)
            if pred[0][0]>0.50:
                return "Tumor"
            else:
                return "not tumor"
    except Exception as e:
        return {"error":str(e)}

    

if __name__=="__main__":
=======
# # Importing essential libraries
# from flask import Flask, render_template,request
# import tensorflow as tf
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy.core.multiarray import array
# app = Flask(__name__)
# @app.route('/predict',methods=["POST"] )
# def predict():
#     model=tf.keras.models.load_model("C:\\Users\\DELL\\Downloads\\cyclone-intensity-estimation-main\\cyclone-intensity-estimation-main\\Model.h5")

#     image=request.files['image']
#     print(image)
#     image.save(image.filename)
#     image = tf.io.read_file(image)
    
#     image = tf.image.decode_image(image, channels=3)
#     resized_image = tf.image.resize(image, (512, 512))
#     preprocessed_image =tf.keras.applications.vgg16.preprocess_input(resized_image)
#     input_data = tf.expand_dims(preprocessed_image, axis=0)
#     a=model.predict(input_data)
#     print(a[0][0])
# if __name__ == '__main__':
# 	app.run(debug=True)

from flask import Flask,request
from flask import Flask, render_template,request
import tensorflow as tf
import cv2
import numpy as np

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def main():
    model=tf.keras.models.load_model("brain_tumor_network.h5")
    try:
        if request.method=='POST':
            image=request.files['image']
            image_name=image.filename
            image.save(image_name)
            img=cv2.imread(image_name)
            img=cv2.resize(img,dsize=(256,256),interpolation=cv2.INTER_CUBIC)
            img=img/255
            image=np.array([img])
            pred=model.predict(image)
            if pred[0][0]>0.50:
                return "Tumor"
            else:
                return "not tumor"
    except Exception as e:
        return {"error":str(e)}

    

if __name__=="__main__":
>>>>>>> 66a425deb85c4a2d874c0186e9b72aa975214865
    app.run("0.0.0.0",debug=True)