from flask import Flask,request
from flask import Flask, render_template,request
import tensorflow as tf
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app=Flask(__name__)

@app.route("/",methods=["POST"])
def main():
    model=tf.keras.models.load_model("brain_tumor_network.h5")
    try:
        if request.method=='POST':
            data = request.json
            a=data["img"]
            bytes_decoded=base64.b64decode(a)
            img=Image.open(BytesIO(bytes_decoded))
            img=img.convert('RGB')
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
    app.run("0.0.0.0",debug=True)
