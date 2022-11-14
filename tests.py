import face_recognition
from PIL import Image
import utils


def run_test(img_path):
    recog_image = face_recognition.load_image_file(img_path)
    face_locations =face_recognition.face_landmarks(recog_image)


    edit_image = Image.open(img_path)
    width, height = edit_image.size

    feature_objs = face_locations[0]

    for key, value in feature_objs.items():
        for indicie in value:
            x = indicie[0]
            y = indicie[1]
            utils.pad_lines(x,y,edit_image, 2)

    edit_image.show()


def run_cheeks_test(img_path):
    edit_image = Image.open(img_path)
    utils.strech_cheeks(edit_image,edit_image,0.5)

