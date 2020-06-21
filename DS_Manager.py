import numpy as np
from PIL import Image, ImageFilter

class DS:
    def __init__(self):
        self.train_x = None
        self.train_y = None
        self.test_x = None
        self.test_x = None
        self.eval_x = None
        self.eval_y = None
class DS_Loader:
    def load_ds(self, address, new_im_size):
        x, y = [], []
        label_idx = dict()
        if os.path.exists(os.path.join(address, ".DS_Store")):
            os.remove(os.path.join(address, ".DS_Store"))
        for i, label in enumerate(os.listdir(address)):
            label_idx[i] = label
            label_address = os.path.join(address, label)

            for image_name in os.listdir(label_address):
                image_address = os.path.join(label_address, image_name)
                try:
                    img = Image.open(image_address).convert('RGB')
                    img = img.resize((new_im_size, new_im_size))
                    x.append(np.array(img, dtype=np.float32))
                    y.append(i)
                except:
                    Log.info("ERROR: can't load {}".format(image_address))

        Log.info(len(x))
        Log.info(len(y))
        return np.stack(x), np.vstack(y), label_idx

