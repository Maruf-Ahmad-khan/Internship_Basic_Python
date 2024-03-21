import matplotlib.pyplot as plt
def imshow(im, title = '', type = '', cv = True):
     if type:
          plt.imshow(im, cmap = type)
     else:
          if cv:
               plt.imshow(im[:,:,::-1])
          else:
               plt.imshow(im)
     plt.title(title)
     plt.axis('off')