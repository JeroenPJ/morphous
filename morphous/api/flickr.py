from morphous import config
from morphous.models.image import Image
import os
import numpy as np
import skimage
import random
import flickrapi

class Flickr:
  def __init__(self):
    self.flickr_api = flickrapi.FlickrAPI(config.FLICKR_API_KEY, config.FLICKR_API_SECRET)
    self.tags = ['green', 'national', 'outside', 'design', 'architecture']
    self.per_page = 50

  def images_from_tag(self, tag = None, max = 100):
    if tag is None:
      tag = random.sample(self.tags, 1)[0]

    response = self.flickr_api.walk(
      tag_mode='all',
      tags=tag,
      extras='url_o',
      per_page=self.per_page,
      sort='relevance'
    )

    images = []
    i = 0
    for img in response:
      url = img.get('url_o')
      if url is not None:
        images.append(Image.from_url(url))

        i += 1
        if i >= max:
          break

    return images
