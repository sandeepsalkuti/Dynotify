from flask import Flask, jsonify, render_template, request
import numpy as np
import cv2
app=Flask("__main__")

@app.route("/upload",methods=["POST","GET"])
def upload():
    if request.method == "POST":
        imagefile1=request.form.get("myFile")
        imagefile2=request.form.get("myFile1")
        if imagefile1 or imagefile2 is None:
            return jsonify({"Error": "Incorrect parameters"})
        img1 = cv2.imread(imagefile1)
        img2 = cv2.imread(imagefile2)
        res = cv2.absdiff(img1, img2)
        res = res.astype(np.uint8)
        percentage = (np.count_nonzero(res) * 100)/ res.size        
        return jsonify({"Percentage" : percentage})
    return render_template('main.html')

if __name__=="__main__":
    app.run(debug=True)


