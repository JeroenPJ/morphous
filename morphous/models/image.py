import numpy as np
import skimage
import matplotlib.pyplot as plt

class Image:
  def __init__(self, np_image):
    self.og_img = np_image
    self.img = np_image

    self.norm_size = (200, 200)
    self.normalize()

  def normalize(self):
    self.img = skimage.transform.resize(self.img, self.norm_size)

  def show(self):
    plt.imshow(self.og_img)
    plt.show()

  @classmethod
  def from_url(klass, url):
    image = skimage.io.imread(url)
    np_image = np.asarray(image, dtype="uint8")
    return klass(np_image)
