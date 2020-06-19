from pptx.enum.shapes import MSO_SHAPE_TYPE


def _get_hash(filename):
    with open(filename, "rb") as f:
        blob = f.read()
    sha1 = hashlib.sha1(blob)
    return sha1.hexdigest()

# See https://github.com/scanny/python-pptx/issues/116
def _replace_img_slide(slide, img, img_path):
    # Replace the picture in the shape object (img) with the image in img_path.

    imgPic = img._pic
    imgRID = imgPic.xpath('./p:blipFill/a:blip/@r:embed')[0]
    imgPart = slide.part.related_parts[imgRID]

    with open(img_path, 'rb') as f:
        rImgBlob = f.read()

    # replace
    imgPart._blob = rImgBlob


def select_all_pictures(slide):
    return [s for s in slide.shapes if s.shape_type == MSO_SHAPE_TYPE.PICTURE]

def remplace_picture(slide, picture_shape, model):
    for picture in models['pictures']:
        if _get_hash(picture) == picture_shape.image.sha1:
            _replace_img_slide(
                slide, picture_shape, models['pictures'][picture]
            )
