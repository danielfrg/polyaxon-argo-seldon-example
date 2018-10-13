import requests
import numpy as np
from PIL import Image

API_AMBASSADOR = "localhost:8003"


def load_image(filename):
    img = Image.open(filename)
    img.load()
    data = np.asarray(img, dtype="int32")
    return data


def rest_request_ambassador(deploymentName, imgpath, endpoint=API_AMBASSADOR):
    arr = load_image(imgpath).flatten()
    shape = arr.shape
    payload = {"data":{"names":[], "tensor":{"shape":shape, "values":arr.tolist()}}}
    response = requests.post(
        "http://"+endpoint+"/seldon/"+deploymentName+"/api/v0.1/predictions",
        json=payload)
    print(response.status_code)
    print(response.text)

rest_request_ambassador("mnist", "images/56.png")
rest_request_ambassador("mnist", "images/87.png")
rest_request_ambassador("mnist", "images/100.png")
