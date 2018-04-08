



from PIL import Image
from SystemUtils import Welcome
import imageio
import numpy as np


"""



"""
class TileProcessor:
    def __init__(self, movie,tile_size, tile_match_res,length ):
        self.movie = movie
        self.length = length
        self.tile_size = tile_size
        self.tile_block_size= tile_size / max(min(tile_match_res, tile_size), 1)
        self.square = int(self.tile_size / self.tile_block_size)


    """

    TODO

    """

    def __process(self, pixels):
        try:

            img = Image.fromarray(pixels, 'RGB')
            w = img.size[0]
            h = img.size[1]
            min_dimension = min(w, h)
            w_crop = (w - min_dimension) / 2
            h_crop = (h - min_dimension) / 2
            img = img.crop((w_crop, h_crop, w - w_crop, h - h_crop))

            large_tile_img = img.resize((self.tile_size, self.tile_size), Image.ANTIALIAS)
            small_tile_img = img.resize((self.square, self.square), Image.ANTIALIAS)

            return (large_tile_img.convert('RGB'), small_tile_img.convert('RGB'))

        except Exception as e:
            #print(colored(traceback.format_exc(), 'red'))
            return (None, None)

    #

    #
    def get_tiles(self):
        large_tiles = []
        small_tiles = []
        l = list()
        print('Reading tiles from \'%s\'...' % (self.movie))
        try:
            vid = imageio.get_reader(self.movie, 'ffmpeg')
            mx =  vid.get_length()
            for x in range(self.length):
                image = vid.get_data(np.random.randint(mx))
                l.append(image)
                Welcome.showAdvance(msg='advance', total=self.length, i=x, outMessage=' Done')





        except Exception as e:
            print(e)

        #progress = ProgressCounter(len(l))

        t = len(l)
        i=0
        for x in l:
            i+=1
            large_tile, small_tile = self.__process(x)
            Welcome.showAdvance(msg='advance',total=t, i=i,outMessage=' Done')
            if large_tile:
                large_tiles.append(large_tile)
                small_tiles.append(small_tile)

        print('Processed %s tiles.' % (len(small_tiles),))
        return (large_tiles, small_tiles)

