from morphous.api import flickr
import random
import numpy as np

class App:
  def __init__(self):
    self.flickr_api = flickr.Flickr()
    self.images = np.array([])
    self.load_batch_size = 5
    self.actions = [
      { 'name': 'load images', 'fn': self.load_images },
      { 'name': 'morph image', 'fn': self.morph },
      { 'name': 'quit', 'fn': self.quit },
    ]

    self.load_images()

  def load_images(self):
    print('loading...')
    new_images = self.flickr_api.images_from_tag(max=self.load_batch_size)
    self.images = np.append(self.images, new_images)

  def print_menu(self):
    print(f'images loaded: {len(self.images)}')
    for i, action in enumerate(self.actions):
      print(f"{i + 1}: {action['name']}")

  def execute(self):
    print('> ', end='')
    action_index = int(input()) - 1
    fn = self.actions[action_index]['fn']
    fn()

  def run(self):
    print('welcome to morpheus!')

    self.running = True
    while self.running:
      self.print_menu()
      self.execute()

  def quit(self):
    print("goodbye!")
    self.running = False

  def morph(self):
    blueprint_index = random.randrange(len(self.images))
    blueprint = self.images[blueprint_index]
    others = self.images[np.arange(len(self.images)) != blueprint_index]
    # select blueprint image
    # split blueprint image
    # while morph_incomplete
    #   load set of images from api
    #   for image in api_images:
    #     compare parts of blueprint image with image
    #     if morph image complete, break
    # show morph_image


